from django import forms
from .models import Category, SubCategory

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name', 'description']

class SubCategoryForm(forms.ModelForm):
	class Meta:
		model = SubCategory
		fields = ['name', 'description', 'category']