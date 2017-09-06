from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.views.generic import TemplateView

from artifacts.forms import ArtifactForm
from artifacts.models import Artifact
from artisans.models import Artisan

import cloudinary
import cloudinary.uploader
import cloudinary.api

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
        return self.render_to_response(context)


class ListArtifactView(TemplateView):
    template_name = 'list_artifact.html'

    def get_context_data(self, **kwargs):
        context = super(ListArtifactView, self).get_context_data(**kwargs)
        context['form'] = ArtifactForm(self.request.POST or None)
        context['artifacts'] = Artifact.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = context['form']
        if form.is_valid():
            artifact = form.save()
            if 'photo' in self.request.FILES:
                filep = self.request.FILES['photo']
                filep.name = str(artifact.pk)
                photo = cloudinary.uploader.upload(filep, public_id=artifact.pk)
                artifact.photo = photo['secure_url']
            artifact.save()
        return self.render_to_response(context)

new_artifact = CreateArtifactView.as_view()
list_artifact = ListArtifactView.as_view()
