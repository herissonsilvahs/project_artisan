from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView, View, UpdateView
from .models import Artisan
from .forms import ArtisanForm
from django.core.urlresolvers import reverse_lazy
from addresses.forms import AddressForm

from artifacts.models import Artifact

import cloudinary
import cloudinary.uploader
import cloudinary.api


class CreateArtisanView(TemplateView):
    template_name = 'new_artisan.html'

    def get_context_data(self, **kwargs):
        context = super(CreateArtisanView, self).get_context_data(**kwargs)
        context['form'] = ArtisanForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = context['form']
        if form.is_valid():
            artisan = form.save()
            if 'photo' in self.request.FILES:
                filep = self.request.FILES['photo']
                filep.name = str(artisan.pk)
                photo = cloudinary.uploader.upload(filep, public_id=artisan.email)
                artisan.photo = photo['secure_url']
            artisan.save()
            return redirect(reverse_lazy('addresses:create', kwargs={'pk': artisan.pk}))
        return self.render_to_response(context)


class ListArtisanView(TemplateView):
    template_name = 'list_artisan.html'

    def get_context_data(self, **kwargs):
        context = super(ListArtisanView, self).get_context_data(**kwargs)
        context['form'] = ArtisanForm(self.request.POST or None)
        context['artisans'] = Artisan.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = context['form']
        if form.is_valid():
            form.save()
        return self.render_to_response(context)


class DetailArtisanView(DetailView):
    model = Artisan
    template_name = 'detail_artisan.html'

    def get_context_data(self, **kwargs):
        context = super(DetailArtisanView, self).get_context_data(**kwargs)
        context['form'] = ArtisanForm(self.request.POST or None, instance=context['artisan'])
        context['form_address'] = AddressForm(self.request.POST or None, instance=context['artisan'].address)
        context['artifacts'] = Artifact.objects.filter(artisan=context['artisan'].pk)[:4]
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        form = context['form']
        form_address = context['form_address']
        if form.is_valid():
            form.save()
        if form_address.is_valid():
            address = form_address.save()
            artisan = get_object_or_404(Artisan, pk=self.object.pk)
            artisan.address = address
            artisan.save()
        return self.render_to_response(context)


class ChangeStatusArtisanView(View):
    status = 0

    def get(self, request, pk):
        artisan = get_object_or_404(Artisan, pk=pk)
        artisan.status = self.status
        artisan.save()
        return redirect(reverse_lazy('artisans:detail', kwargs={'pk': artisan.pk}))


new = CreateArtisanView.as_view()
list_artisan = ListArtisanView.as_view()
detail = DetailArtisanView.as_view()
activate = ChangeStatusArtisanView.as_view()
deactivate = ChangeStatusArtisanView.as_view(status=1)
block = ChangeStatusArtisanView.as_view(status=2)
