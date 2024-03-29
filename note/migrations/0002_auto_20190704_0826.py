# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-04 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='user',
            new_name='author',
        ),
        migrations.AddField(
            model_name='note',
            name='mod_time',
            field=models.DateField(auto_now=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='note',
            name='create_time',
            field=models.DateField(auto_now_add=True, verbose_name='创建时间'),
        ),
    ]
