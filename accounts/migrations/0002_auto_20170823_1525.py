# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.CharField(default='https://res.cloudinary.com/dlr1vmgpr/image/upload/v1503512687/avatar_g4vll9.png', max_length=350, verbose_name='Avatar'),
        ),
    ]
