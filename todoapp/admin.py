from django.contrib import admin
from .models import *


class todoAdmin(admin.ModelAdmin):
    # list_display = ['id', 'task', 'owner']
    # search_fields = ['task', 'owner']
    list_display = ['id', 'task', 'owner', 'created_at', 'last_updated_on']
    search_fields = ['task', 'owner', 'created_at', 'last_updated_on']
    list_display_links = ['task']
    list_filter = ['owner']
    list_per_page = 5


# Register your models here. Will be able to view this from the django's administration panel
admin.site.register(MyTodo, todoAdmin)
