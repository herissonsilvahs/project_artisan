from django.db import models
from addresses.models import Address

# Create your models here.

class Artisan(models.Model):
	ACTIVATED = 0
	DISABLED = 1
	BLOCKED = 2
	STATUS = (
        (ACTIVATED, 'activated'),
        (DISABLED, 'disabled'),
        (BLOCKED, 'blocked'),
    )

	name = models.CharField('Nome', max_length=150)
	email = models.CharField('Email', max_length=90)
	photo = models.CharField('Foto', max_length=200, default="http://res.cloudinary.com/dlr1vmgpr/image/upload/v1503512788/avatar_art_hnzs69.jpg")
	phone = models.CharField('Telefone', max_length=30)
	phone_optional = models.CharField('Telefone Opcional', max_length=30)
	cpf = models.CharField('CPF', max_length=15)
	biography = models.TextField('Biografia')
	status = models.IntegerField('Status', choices=STATUS, default=ACTIVATED)
	address = models.ForeignKey(Address, verbose_name='Endereço', null=True)

	class Meta:
		verbose_name = 'Artesão'
		verbose_name_plural = 'Artesãos'
		ordering = ['name']