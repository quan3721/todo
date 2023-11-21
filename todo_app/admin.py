from django.contrib import admin
from .models import Task

# Edit in admin page #
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at')
    search_fields = ('task',) # search box


# Register your models here.
admin.site.register(Task, TaskAdmin)