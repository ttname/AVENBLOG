#! /usr/bin/env python
# -*- coding: utf-8
import logging
from django.shortcuts import render
from app.models import *
from django.conf import settings
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.views.generic import View
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from collections import Counter
logger = logging.getLogger(__name__)

class BaseMixin(object):

    def get_context_data(self, *args, **kwargs):
	context = super(BaseMixin,self).get_context_data(**kwargs)
        if 'object' not in kwargs or 'query' in kwargs:
            try:
                context['categories'] = Category.objects.all() #得到分类
		context['aboutme'] = {'aboutme': settings.ABOUT_ME} # 得到其他配置
		context['alltags'] = Blog.all_tags()
            except Exception as e:
                logger.exception(u'加载基本信息出错[%s]！', e)
        return context




class IndexView(BaseMixin,ListView):
    template_name = 'home.html'
    context_object_name = 'article_list'

    def get_context_data(self, **kwargs):
	context = super(IndexView, self).get_context_data(**kwargs)
	context['article_list'] = self.article_list
        return context


    def get(self, request, *args, **kwargs):
        try:
            self.cur_page = int(request.GET.get('page', 1))
        except TypeError:
            self.cur_page = 1
        if self.cur_page < 1:
            self.cur_page = 1
        return super(IndexView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        article_lists = Blog.objects.filter(status=0)
        paginator = Paginator(article_lists, 2)
        self.article_list = paginator.page(self.cur_page)
	return self.article_list

class CategoryListView(IndexView):


    def get_context_data(self, **kwargs):
	context = super(CategoryListView, self).get_context_data(**kwargs)
	context['article_list'] = self.article_list
        context['title'] = Category.objects.get(id=self.id).name + ' |'
	print context['title']
        return context


    def get(self, request,*args, **kwargs):
        try:
            self.cur_page = int(request.GET.get('page', 1))
        except TypeError:
            self.cur_page = 1
        if self.cur_page < 1:
            self.cur_page = 1
        self.id = kwargs.get('id')
        return super(CategoryListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        article_lists = Blog.objects.filter(category_id=self.id)
        paginator = Paginator(article_lists, 2)
        self.article_list = paginator.page(self.cur_page)
	return self.article_list


class  PageView(BaseMixin,DetailView):
    template_name = 'detail.html'
    context_object_name = 'article'
    queryset=Blog.objects.filter(status=0)
    
    def get_context_data(self, **kwargs):
        context  = super(PageView, self).get_context_data(**kwargs)
	context['article'] = self.object
	context['categories'] = Category.objects.all()
	context['alltags'] = Blog.all_tags()
        return context
 

    def get_object(self):
	object = super(PageView, self).get_object()
	return object

class TagsListView(IndexView):

    def get_queryset(self):
        self.tag = self.kwargs.get('tag')
        article_lists = Blog.objects.defer('body', 'body').filter(tags__icontains=self.tag, status=0)
	paginator = Paginator(article_lists, 2)
        self.article_list = paginator.page(self.cur_page)
        return self.article_list


    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['article_list'] = self.article_list
	context['title'] = self.tag + ' | '
        return context


    def get(self, request, *args, **kwargs):
        try:
            self.cur_page = int(request.GET.get('page', 1))
        except TypeError:
            self.cur_page = 1
        if self.cur_page < 1:
            self.cur_page = 1
        return super(IndexView, self).get(request, *args, **kwargs)


def AboutMe(request):
    return render(request, 'about_me.html')



