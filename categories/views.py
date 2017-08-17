from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView, View, DeleteView
from .forms import CategoryForm
from .models import Category
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class ListCategoryView(TemplateView):
	template_name = 'list_category.html'

	def get_context_data(self, **kwargs):
		context = super(ListCategoryView, self).get_context_data(**kwargs)
		context['form'] = CategoryForm(self.request.POST or None)
		context['categories'] = Category.objects.all()
		return context

	def post(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		form = context['form']
		if form.is_valid:
			form.save()
		return self.render_to_response(context)

class DetailCategoryView(DetailView):
	model = Category
	template_name = 'detail_category.html'

	def get_context_data(self, **kwargs):
		context = super(DetailCategoryView, self).get_context_data(**kwargs)
		context['form'] = CategoryForm(self.request.POST or None, instance=context['category'])
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		context = self.get_context_data(object=self.object)
		form = context['form']
		if form.is_valid():
			form.save()
		return self.render_to_response(context)

class DeleteCategoryView(DeleteView):
	template_name = 'delete_category.html'
	model = Category
	context_object_name = 'category'
	success_url = reverse_lazy('categories:list')



list_category = ListCategoryView.as_view()
detail = DetailCategoryView.as_view()
delete = DeleteCategoryView.as_view()
