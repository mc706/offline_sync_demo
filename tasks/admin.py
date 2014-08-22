from django.contrib import admin
from tasks.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['key', 'account', 'title', 'completed', 'deleted', 'date_modified']
    search_fields = ['title']
    list_filter = ['account', 'completed']