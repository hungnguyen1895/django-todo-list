# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


# Create your models here.
class Task(models.Model):

	#problem is to set the current user to the task
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	task_name = models.CharField(max_length=30)
	description = models.CharField(max_length=50)
	is_completed = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('task:index')
