from django.contrib import admin
from .models import *


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'task']
    search_fields = ['task']
    list_display_links = ['task']
    list_per_page = 5


# Register your models here. Will be able to view this from the django's administration panel
admin.site.register(MyTodo)
