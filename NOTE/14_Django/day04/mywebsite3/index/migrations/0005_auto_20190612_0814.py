# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-12 08:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20190612_0812'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'author', 'verbose_name_plural': 'author'},
        ),
    ]