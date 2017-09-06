from django.db import models

# Create your models here.
from artisans.models import Artisan
from categories.models import Material


class Artifact(models.Model):
    name = models.CharField('Nome', max_length=150)
    description = models.TextField('Descrição')
    photo = models.CharField('Foto', max_length=200,
                             default="http://res.cloudinary.com/dlr1vmgpr/image/upload/v1503512788/avatar_art_hnzs69.jpg")
    material = models.ForeignKey(Material, verbose_name='Material', null=True)
    artisan = models.ForeignKey(Artisan, verbose_name='Material', null=False)

    def get_summary(self):
        return self.description[:50]+'...'
