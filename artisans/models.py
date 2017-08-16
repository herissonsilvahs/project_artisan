from django.db import models

# Create your models here.

class Artisan(models.Model):
	name = models.CharField('Nome', max_length=150)
	email = models.CharField('Email', max_length=90)
	photo = models.CharField('Foto', max_length=200)
	phone = models.CharField('Telefone', max_length=30)
	phone_optional = models.CharField('Telefone Opcional', max_length=30)
	cpf = models.CharField('CPF', max_length=15)
	biography = models.TextField('Biografia', max_length=250)

	class Meta:
		verbose_name = 'Artesão'
		verbose_name_plural = 'Artesãos'
		ordering = ['name']