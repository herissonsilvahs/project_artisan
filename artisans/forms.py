from django import forms
from .models import Artisan

class ArtisanForm(forms.ModelForm):
	class Meta:
		model = Artisan
		fields = ['name', 'email', 'photo', 'phone', 'phone_optional', 'cpf', 'biography']