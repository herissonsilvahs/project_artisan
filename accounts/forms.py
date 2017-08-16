from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
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

class AuthenticationFormWithChekUsersStatus(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.status == 0:
            raise forms.ValidationError(
                ("Sua conta está desabilitada!"),
                code='inactive',
            )