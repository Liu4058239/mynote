# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-04 11:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
