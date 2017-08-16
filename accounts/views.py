from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, View
from .forms import UserCreateForm, UserUpdateForm

from .models import User
from addresses.forms import AddressForm 

from django.contrib.auth.mixins import LoginRequiredMixin
from .polices import IsRoot, IsAdm

from django.contrib.auth.views import LoginView
from .forms import AuthenticationFormWithChekUsersStatus

class LoginCustomView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationFormWithChekUsersStatus

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

class ListUserView(LoginRequiredMixin, IsAdm, TemplateView):
	template_name = 'list_user.html'
	context_object_name = 'users'

	def get_context_data(self, **kwargs):
		context = super(ListUserView, self).get_context_data(**kwargs)
		context['form_create'] = UserCreateForm(self.request.POST or None)
<<<<<<< HEAD
=======
		context['users'] = User.objects.all()
>>>>>>> e7732337915a99cc50ab7d3aed3a840e21e6a75f
		return context

	def post(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		form = context['form_create']
		if form.is_valid():
			form.save()
		return self.render_to_response(context)

class DetailUserView(LoginRequiredMixin, IsAdm, DetailView):
	model = User
	template_name = 'detail_user.html'
	context_object_name = 'user_request'

	def get_context_data(self, **kwargs):
		context = super(DetailUserView, self).get_context_data(**kwargs)
		context['form_update'] = UserUpdateForm(self.request.POST or None, instance=context['user_request'])
		context['form_address'] = AddressForm(self.request.POST or None, instance=context['user_request'].address)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		context = self.get_context_data(object=self.object)
		form = context['form_update']
		form_address = context['form_address']
		if form.is_valid():
			form.save()
		if form_address.is_valid():
			address = form_address.save()
			user_request = get_object_or_404(User, pk=self.object.pk)
			user_request.address = address
			user_request.save()
		return self.render_to_response(context)

class ChangeStatusUserView(LoginRequiredMixin, IsAdm, View):
	status = 0
	def get(self, request, pk):
		user = get_object_or_404(User, pk=pk)
		user.status = self.status
		user.save()
		return redirect(reverse_lazy('accounts:detail', kwargs={'pk':user.pk}))

  

  
login = LoginCustomView.as_view()
dashboard = DashboardView.as_view()
list_user = ListUserView.as_view()
detail = DetailUserView.as_view()
activate = ChangeStatusUserView.as_view()
deactivate = ChangeStatusUserView.as_view(status=1)
block = ChangeStatusUserView.as_view(status=2)
