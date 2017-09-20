from django.shortcuts import render
from django.views.generic import TemplateView
from artifacts.models import Artifact
from artisans.models import Artisan


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['artifacts'] = Artifact.objects.all()[:5]
        context['artifacts_count'] = Artifact.objects.count()
        context['artisans_count'] = Artisan.objects.count()
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

index = IndexView.as_view()
about = AboutView.as_view()
