import os, sys
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import login as django_login, logout as django_logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils.http import is_safe_url
from konstantin.utils import get_client_ip 
from konstantin.stuff.models import Project
from konstantin.stuff.enums import ProjectType, ProjectState
from konstantin.blog.models import BlogPost
from .models import Admin
from .forms import AdminLoginForm

def home(request):
    """
    #TODO: auto redirect after a few seconds.
    """
    ip = get_client_ip(request)
    return render(request, 'home/home.html', {
        "client_ip": ip,
    })

@login_required
def admin(request):
    """
    #TODO: add more stuff. (edit buttons, bio, work, contact)
    """
    projects = Project.objects.all()
    blog = BlogPost.objects.all()
    return render(request, 'home/admin.html', {
        'ProjectType': ProjectType,
        'ProjectState': ProjectState,
        'projects': projects,
        'blog': blog,
    })


def admin_login(request):
    """
    general login
    """
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('admin'))
    if request.POST:
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            django_login(request, form.cleaned_data['user'])
            safe_url = reverse('admin')
            url = form.cleaned_data.get("next", safe_url)
            if is_safe_url(url, host=request.get_host()):
                return HttpResponseRedirect(url)

            return HttpResponseRedirect(safe_url)
    else:
            form = AdminLoginForm(initial=request.GET)

    return render(request, 'home/admin_login.html', {
        "form": form,
    })

