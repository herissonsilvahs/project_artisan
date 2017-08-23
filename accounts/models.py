from django.db import models

from django.db import models
from addresses.models import Address
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
import re

class User(AbstractBaseUser, PermissionsMixin):
    
    ROOT = 0
    ADM = 1
    SUPPORT = 2
    TYPES = (
    (ROOT, 'root'),
    (ADM, 'Administrador'),
    (SUPPORT, 'Suporte')
    )

    ACTIVATED = 0
    DISABLED = 1
    BLOCKED = 2
    STATUS = (
        (ACTIVATED, 'activated'),
        (DISABLED, 'disabled'),
        (BLOCKED, 'blocked'),
    )
    name = models.CharField('Nome', max_length=150)
    email = models.EmailField('Email', unique=True)
    phone = models.CharField('Telefone', max_length=40, null=True)
    phoneOptional = models.CharField('Telefone Opcional', max_length=40, null=True)
    status = models.IntegerField('Status', choices=STATUS, default=ACTIVATED)
    username = models.CharField('Usuário', max_length=30, unique=True, validators=[
    validators.RegexValidator(
        re.compile('^[\w.@+-]+$'),
            'Informe o nome de usuário válido',
            'Este valor deve conter apenas letras, números '
            'e os caracteres: @/./+/-/_ .',
            'Inválido'
            )
        ], help_text='Um nome curto que será usado para identificá-lo de forma única no sistema'
    )
    nivel = models.IntegerField('Nível', choices=TYPES, default=SUPPORT)
    address = models.ForeignKey(Address, verbose_name='Endereço', null=True)
    photo = models.CharField('Avatar', max_length=350, default="https://res.cloudinary.com/dlr1vmgpr/image/upload/v1503512687/avatar_g4vll9.png")
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]