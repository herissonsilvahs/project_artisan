from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from artisans.models import Artisan
from .forms import AddressForm
from django.core.urlresolvers import reverse_lazy

class CreateAddressView(TemplateView):
    template_name = 'new_address.html'

    def get_context_data(self, **kwargs):
        context = super(CreateAddressView, self).get_context_data(**kwargs)
        context['form'] = AddressForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = context['form']
        if form.is_valid():
            address = form.save()
            pk_artisan = context['pk']
            artisan = get_object_or_404(Artisan, pk=pk_artisan)
            artisan.address = address
            artisan.save()
        return redirect(reverse_lazy('artisans:detail', kwargs={'pk':pk_artisan}))

create = CreateAddressView.as_view()