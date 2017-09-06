from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy

# Create your views here.
from django.views.generic import TemplateView, ListView

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
        return redirect(reverse_lazy('artisans:detail', kwargs={'pk': artisan.pk}))


class ListArtifactView(ListView):
    model = Artifact
    context_object_name = 'artifacts'
    template_name = 'list_artifact.html'
    paginate_by = 20



new_artifact = CreateArtifactView.as_view()
list_artifact = ListArtifactView.as_view()
