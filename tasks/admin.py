from django.contrib import admin
from tasks.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['key', 'account', 'title', 'completed']
    search_fields = ['title']
    list_filter = ['account', 'completed']


admin.site.register(Task, TaskAdmin)