# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-04 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_auto_20190704_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='标题'),
        ),
    ]
