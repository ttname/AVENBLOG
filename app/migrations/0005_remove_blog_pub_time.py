# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 08:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160225_0801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='pub_time',
        ),
    ]
