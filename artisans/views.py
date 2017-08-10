from django.shortcuts import render
from django.views.generic import CreateView
from .models import Artisan
from .forms import ArtisanForm
from django.core.urlresolvers import reverse_lazy

class CreateArtisanView(CreateView):
	template_name = 'new_artisan.html'
	model = Artisan
	form_class = ArtisanForm
	success_url = reverse_lazy('accounts:list')



new = CreateArtisanView.as_view()