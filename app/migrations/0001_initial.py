# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 03:50
from __future__ import unicode_literals

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackendCkeditor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor.fields.RichTextField(verbose_name='\u5185\u5bb9')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('body', ckeditor.fields.RichTextField(verbose_name='\u5185\u5bb9')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('tags', models.CharField(blank=True, help_text='\u7528\u82f1\u6587\u9017\u53f7\u5206\u5272', max_length=100, null=True, verbose_name='\u6807\u7b7e')),
                ('status', models.IntegerField(choices=[(0, '\u6b63\u5e38'), (1, '\u8349\u7a3f'), (2, '\u5220\u9664')], default=0, verbose_name='\u72b6\u6001')),
                ('pub_time', models.DateTimeField(default=datetime.datetime(2016, 2, 23, 11, 50, 7, 316000), verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='\u540d\u79f0')),
                ('status', models.IntegerField(choices=[(0, '\u6b63\u5e38'), (1, '\u8349\u7a3f'), (2, '\u5220\u9664')], default=0, verbose_name='\u72b6\u6001')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category', verbose_name='\u5206\u7c7b'),
        ),
    ]