import os, shutil, sys, datetime
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib import messages
from django.db.models import F
from django.db import transaction, DatabaseError
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from .models import File

def list_(request):
	"""
	list all files
	"""
	files = File.objects.all()
	return render(request, 'files/list.html', {
		"files": files,
	})

def delete(request):
	pass

def upload(request):
	pass
