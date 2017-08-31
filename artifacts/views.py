from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from artifacts.forms import ArtifactForm
from artifacts.models import Artifact

import cloudinary
import cloudinary.uploader
import cloudinary.api


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

list_artifact = ListArtifactView.as_view()
