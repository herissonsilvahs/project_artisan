from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, DeleteView

from artifacts.forms import ArtifactForm
from artifacts.models import Artifact
from artisans.models import Artisan
from categories.models import Category, SubCategory, Material

import cloudinary
import cloudinary.uploader
import cloudinary.api

from comments.forms import CommentForm
from comments.models import Comment


class CreateArtifactView(TemplateView):
    template_name = 'new_artifact.html'

    def get_context_data(self, **kwargs):
        context = super(CreateArtifactView, self).get_context_data(**kwargs)
        context['form'] = ArtifactForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = context['form']
        if form.is_valid():
            pk_artisan = context['pk']
            artisan = get_object_or_404(Artisan, pk=pk_artisan)
            artifact = form.save(commit=False)
            artifact.artisan = artisan
            artifact = form.save()
            if 'photo' in self.request.FILES:
                filep = self.request.FILES['photo']
                filep.name = str(artifact.pk)
                photo = cloudinary.uploader.upload(filep, public_id=artifact.pk)
                artifact.photo = photo['secure_url']
            artifact.save()
        return redirect(reverse_lazy('artisans:detail', kwargs={'pk': artisan.pk}))


class ListArtifactView(ListView):
    model = Artifact
    context_object_name = 'artifacts'
    template_name = 'list_artifact.html'
    paginate_by = 20


class DetailArtifactView(DetailView):
    model = Artifact
    template_name = 'detail_artifact.html'

    def get_context_data(self, **kwargs):
        context = super(DetailArtifactView, self).get_context_data(**kwargs)
        context['form'] = ArtifactForm(self.request.POST or None, instance=context['artifact'])
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        form = context['form']
        if form.is_valid():
            form.save()
        return self.render_to_response(context)


class DeleteArtifactView(DeleteView):
    template_name = 'delete_artifact.html'
    model = Artifact
    context_object_name = 'artifact'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        artifact = context['artifact']
        artisan_pk = artifact.artisan.pk
        if artifact.delete():
            return redirect(reverse_lazy('artisans:detail', kwargs={'pk': artisan_pk}))


class ArtifactListUsersView(ListView):
    model = Artifact
    template_name = 'list_artifact_for_user.html'
    context_object_name = 'artifacts'
    paginate_by = 10

    def get_queryset(self):
        queryset = Artifact.objects.all()
        order_by = self.request.GET.get('order_by', '')
        order = self.request.GET.get('order', '')
        if order_by == 'categoria':
            queryset = Artifact.objects.filter(subcategory__category=order)
        elif order_by == 'sub_categoria':
            queryset = Artifact.objects.filter(subcategory=order)
        elif order_by == 'material':
            queryset = Artifact.objects.filter(material=order)
        elif self.request.GET.get('search', ''):
            queryset = Artifact.objects.filter(name__icontains=self.request.GET.get('search', ''))

        return queryset



    def get_context_data(self, **kwargs):
        context = super(ArtifactListUsersView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['sub_categories'] = SubCategory.objects.all()
        context['materials'] = Material.objects.all()
        return context


class ArtifactShowUserView(DetailView):
    model = Artifact
    template_name = 'show_artifact_for_user.html'
    context_object_name = 'artifact'

    def get_context_data(self, **kwargs):
        context = super(ArtifactShowUserView, self).get_context_data(**kwargs)
        query = Artifact.objects.filter(subcategory=self.get_object().subcategory.pk)
        context['related_artifacts'] = query.exclude(pk=self.get_object().pk)
        context['form_comment'] = CommentForm(self.request.POST or None)
        context['comments'] = Comment.objects.filter(artifact=self.get_object().pk)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        form_comment = context['form_comment']
        if form_comment.is_valid():
            comment = form_comment.save(commit=False)
            comment.artifact = self.get_object()
            comment.save()

        return self.render_to_response(context)


new_artifact = CreateArtifactView.as_view()
list_artifact = ListArtifactView.as_view()
detail_artifact = DetailArtifactView.as_view()
delete_artifact = DeleteArtifactView.as_view()
list_artifact_users = ArtifactListUsersView.as_view()
show_artifact_user = ArtifactShowUserView.as_view()
