from django import forms
from .models import Artisan

class ArtisanForm(forms.ModelForm):
	class Meta:
		model = Artisan
		fields = ['name', 'email', 'phone', 'phone_optional', 'cpf', 'biography']