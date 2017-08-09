from django.db import models

class Address(models.Model):
    zipcode = models.CharField('CEP', max_length=9)
    street = models.CharField('Rua', max_length=200)
    number = models.CharField('Número', max_length=30)
    neighborhood = models.CharField('Bairro', max_length=100)
    city = models.CharField('Cidade', max_length=100)
    state = models.CharField('Estado', max_length=3)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ['city']