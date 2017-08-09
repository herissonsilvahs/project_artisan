from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
	template_name = 'navbar.html'

index = IndexView.as_view()
