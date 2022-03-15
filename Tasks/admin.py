from django.contrib import admin
from .models import Task
# Register your models here.


@admin.register(Task)
class TasksAd(admin.ModelAdmin):
    list_display = ['name','priority','status']
