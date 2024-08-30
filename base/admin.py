from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'complete')
    search_fields = ('title', 'description')

admin.site.register(Task, TaskAdmin)
