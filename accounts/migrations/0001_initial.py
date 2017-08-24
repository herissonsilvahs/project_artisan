# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 17:41
from __future__ import unicode_literals

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addresses', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone', models.CharField(max_length=40, null=True, verbose_name='Telefone')),
                ('phoneOptional', models.CharField(max_length=40, null=True, verbose_name='Telefone Opcional')),
                ('status', models.IntegerField(choices=[(0, 'Ativado'), (1, 'Desativado'), (2, 'Bloqueado')], default=0, verbose_name='Status')),
                ('username', models.CharField(help_text='Um nome curto que será usado para identificá-lo de forma única no sistema', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'Informe o nome de usuário válido', 'Este valor deve conter apenas letras, números e os caracteres: @/./+/-/_ .', 'Inválido')], verbose_name='Usuário')),
                ('nivel', models.IntegerField(choices=[(0, 'root'), (1, 'Administrador'), (2, 'Suporte')], default=2, verbose_name='Nível')),
                ('photo', models.CharField(default='https://res.cloudinary.com/dlr1vmgpr/image/upload/v1503512687/avatar_g4vll9.png', max_length=350, verbose_name='Avatar')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Equipe')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='addresses.Address', verbose_name='Endereço')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'ordering': ['name'],
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
