import os, sys
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Project, ProjectFile
from .forms import ProjectForm
from .tasks import get_screenshot
from .enums import ProjectType, ProjectState, ProjectRole

# Create your views here.

def list(request):

	projects = Project.objects.all()
	project_files = ProjectFile.objects.all()	
	return render(request, 'stuff/list.html', {
		'projects': projects,
                'ProjectState': ProjectState,
                'ProjectRole': ProjectRole,
                'ProjectType': ProjectType,
		'project_files': project_files,
	})

@login_required
def create(request):
	return _edit(request, project_id=None)

@login_required
def edit(request, project_id):
	return _edit(request, project_id)

def _edit(request, project_id):
    """

    """
    if project_id is None:
        project = None
    else:
        project = get_object_or_404(Project, pk=project_id)

    if request.POST:
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('stuff'))
    else:
        form = ProjectForm(instance=project)

    return render(request, 'stuff/edit.html', {
            'form': form,
    })	

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    return HttpResponseRedirect(reverse('stuff'))

def contact(request):
    
    return render(request, 'stuff/contact.html', {
        
    })
