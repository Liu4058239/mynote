from django.contrib import admin
from . import models


# Register your models here.

class UserManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'password','email']
    list_filter = ['name']
    search_fields = ['id', 'name']
    list_editable = ['name']


admin.site.register(models.User, UserManager)
