from django.db import models

class Category(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição', max_length=400)

    def __str__(self):
    	return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

	

class SubCategory(models.Model):
	name = models.CharField('Nome', max_length=50)
	description = models.TextField('Descrição', max_length=400)
	category = models.ForeignKey(Category, verbose_name='Categoria', null=True, on_delete=models.SET_NULL)

	class Meta:
		verbose_name = 'Subcategoria'
		verbose_name_plural = 'Subcategorias'
		ordering = ['name']
