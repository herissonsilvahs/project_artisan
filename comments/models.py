from django.db import models

from artifacts.models import Artifact


class Comment(models.Model):
    name = models.CharField('Nome', max_length=150)
    comment = models.TextField('Comentario')
    artifact = models.ForeignKey(Artifact, verbose_name='Artesanato', on_delete=models.CASCADE, null=True, related_name='comment')
    created = models.DateTimeField('Criado em', auto_now_add=True)