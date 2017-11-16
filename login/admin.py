from django.contrib import admin
from login.models import *
# Register your models here.
# class Myadmin(admin.ModelAdmin):
#     list_display = ['name','sex']
admin.site.register(User)
