# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-14 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20, verbose_name='用户名')),
                ('upwd', models.CharField(max_length=50, verbose_name='密码')),
                ('uemail', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('uphone', models.CharField(max_length=11, verbose_name='手机')),
                ('isActive', models.BooleanField(default=True, verbose_name='状态')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
