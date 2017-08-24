# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 17:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artisan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
                ('email', models.CharField(max_length=90, verbose_name='Email')),
                ('photo', models.CharField(default='http://res.cloudinary.com/dlr1vmgpr/image/upload/v1503512788/avatar_art_hnzs69.jpg', max_length=200, verbose_name='Foto')),
                ('phone', models.CharField(max_length=30, verbose_name='Telefone')),
                ('phone_optional', models.CharField(max_length=30, verbose_name='Telefone Opcional')),
                ('cpf', models.CharField(max_length=15, verbose_name='CPF')),
                ('biography', models.TextField(verbose_name='Biografia')),
                ('status', models.IntegerField(choices=[(0, 'activated'), (1, 'disabled'), (2, 'blocked')], default=0, verbose_name='Status')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='addresses.Address', verbose_name='Endereço')),
            ],
            options={
                'verbose_name': 'Artesão',
                'ordering': ['name'],
                'verbose_name_plural': 'Artesãos',
            },
        ),
    ]