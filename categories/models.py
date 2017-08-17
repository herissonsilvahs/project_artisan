from django.db import models

class Category(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição', max_length=400)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']