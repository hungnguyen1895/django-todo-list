# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
	list_display = ['user', 'task_name', 'description', 'is_completed']
	
admin.site.register(Task, TaskAdmin)