#! /usr/bin/env python
# -*- coding: utf-8

from __future__ import unicode_literals
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
import datetime


STATUS = {
    0: u'正常',
    1: u'草稿',
    2: u'删除',
}




class Tag(models.Model):
    tag_name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.tag_name

class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'名称')
    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name=u'状态')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)

    def __unicode__(self):
        return '%s' % (self.name)



    def available_list(cls):
        return cls.objects.filter(status=1)

    class Meta:
        verbose_name_plural = verbose_name = u"分类"


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'标签', help_text=u'用英文逗号分割')
    category = models.ForeignKey(Category, verbose_name=u'分类')
    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name=u'状态')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)

    body = RichTextField(verbose_name="内容")

    def __unicode__(self):
        return '%s' %self.title

    def tags_list(self):
        return [tag.strip() for tag in self.tags.split(',')]

    def get_tags(aa):
	print '1-----------------1'
        return aa.objects.all()

    @classmethod 
    def all_tags(cls):
        alltag = cls.objects.defer("title","body")

        a=[]
	c={}
	for i in alltag:
	    for ii in i.tags.split(','):
		a.append(ii);
	for i in a:
            c[i] = a.count(i)
	return c

    def get_absolute_url(self):
        return '/%s/' % ( self.id)

    def next_post(self):
        # 下一篇
        return Blog.objects.filter(id__gt=self.id, status=0).order_by('id').first()


    def prev_post(self):
        # 前一篇
        return Blog.objects.filter(id__lt=self.id, status=0).first()

    class Meta:
        ordering = ['-timestamp']

class BackendCkeditor(models.Model):
    body = RichTextField(verbose_name="内容")
