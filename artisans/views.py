from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .models import Artisan
from .forms import ArtisanForm
from django.core.urlresolvers import reverse_lazy

class CreateArtisanView(CreateView):
	template_name = 'new_artisan.html'
	model = Artisan
	form_class = ArtisanForm
	success_url = reverse_lazy('accounts:list')

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

new = CreateArtisanView.as_view()
list_artisan = ListArtisanView.as_view()