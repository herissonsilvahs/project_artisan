from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

#Form para criação de usuário
class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'phone', 'phoneOptional', 'status', 'nivel']

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'name', 'phone', 'phoneOptional', 'status', 'nivel']