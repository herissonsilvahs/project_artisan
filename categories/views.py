from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import CategoryForm
from .models import Category

# Create your views here.
class ListCategoryView(TemplateView):
	template_name = 'list_category.html'

	def get_context_data(self, **kwargs):
		context = super(ListCategoryView, self).get_context_data(**kwargs)
		context['form'] = CategoryForm(self.request.POST or None)
		context['categories'] = Category.objects.all()
		return context



list_category = ListCategoryView.as_view()
