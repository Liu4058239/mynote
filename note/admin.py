from django.contrib import admin
from . import models
# Register your models here.

class NoteManager(admin.ModelAdmin):
    list_display = ['id','title','content','create_time','mod_time']
    list_filter = ['title']
    search_fields = ['id','title']
    # list_editable = ['content','create_time']

admin.site.register(models.Note,NoteManager)
