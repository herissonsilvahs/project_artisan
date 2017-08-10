from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, View
from .forms import UserCreateForm, UserUpdateForm
from .models import User

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

class ListUserView(TemplateView):
	template_name = 'list_user.html'

	def get_context_data(self, **kwargs):
		context = super(ListUserView, self).get_context_data(**kwargs)
		context['form_create'] = UserCreateForm(self.request.POST or None)

		context['users'] = User.objects.all()
		return context

	def post(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		form = context['form_create']
		if form.is_valid():
			form.save()
		return self.render_to_response(context)

class DetailUserView(DetailView):
	model = User
	template_name = 'detail_user.html'
	context_object_name = 'user_request'

	def get_context_data(self, **kwargs):
		context = super(DetailUserView, self).get_context_data(**kwargs)
		context['form_update'] = UserUpdateForm(self.request.POST or None, instance=context['user_request'])
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		context = self.get_context_data(object=self.object)
		form = context['form_update']
		if form.is_valid():
			form.save()
		return self.render_to_response(context)

class ChangeStatusUserView(View):
	status = 0
	def get(self, request, pk):
		user = get_object_or_404(User, pk=pk)
		user.status = self.status
		user.save()
		return redirect(reverse_lazy('accounts:detail', kwargs={'pk':user.pk}))


dashboard = DashboardView.as_view()
list_user = ListUserView.as_view()
detail = DetailUserView.as_view()
activate = ChangeStatusUserView.as_view()
deactivate = ChangeStatusUserView.as_view(status=1)
block = ChangeStatusUserView.as_view(status=2)
