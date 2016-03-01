#coding=utf-8
from django import template
import json
register = template.Library()


from django import template
register = template.Library()
def do_list(value):
    return range(1, value+1)
register.filter('do_list',do_list)