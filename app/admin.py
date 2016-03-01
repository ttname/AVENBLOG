from django.contrib import admin
from blog import settings
from app.models import *

# Register your models here.
admin.site.register(BackendCkeditor)
admin.site.register(Blog)


admin.site.register(Category)