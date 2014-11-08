import os, sys, re
from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model, authenticate
from django.db import connection
from .models import Admin as User

class AdminLoginForm(forms.Form):
	"""
	Basic login form for admin. No creation form,
	as it will be manually entered into the database.
	"""
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self):
		""" Validate form """
		cleaned_data = super(AdminLoginForm, self).clean()
		user_model = get_user_model()
		next = forms.CharField(widget=forms.HiddenInput, required=False)

		username = cleaned_data.get("username")
		password = cleaned_data.get("password")
		if username and password:
			user = authenticate(username=username, password=password)
			if user is not None:
				if not (user.first_name.lower() == "konstantin") and (user.last_name.lower() == "farrell"):
					raise forms.ValidationError("Get off my site.")
				else:
					cleaned_data['user'] = user
			else:
				raise forms.ValidationError("Incorrect Password")
		return cleaned_data
		
