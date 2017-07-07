# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib.auth import logout

# Create your views here.

@login_required
def dashboard(request):
	return render(request, 'account/dashboard.html')

def register(request):

	logout(request)

	if request.method == 'GET':
		form = UserRegistrationForm()
		return render(request, 'account/register.html', {'form': form})
	elif request.method == 'POST':
		form = UserRegistrationForm(request.POST)

		if form.is_valid():
			#create a user object but not saving yet
			user = form.save(commit=False)

			#set password and save user object
			user.set_password(form.cleaned_data['password'])
			user.save()

			return render(request, 'account/register_done.html', {'user': user})

	