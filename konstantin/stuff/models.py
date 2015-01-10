import os, sys, re, shutil, hashlib
from django.conf import settings
from django.db import models
from konstantin.files.models import File


class Project(models.Model):
    """
    Basic model for a project
    """

    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    description = models.TextField()
    role = models.TextField()
    type = models.IntegerField()   
    current_state = models.IntegerField()

    date_added = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(auto_now=False, blank=True)
    team = models.CharField(max_length=255)
    screenshot = models.ImageField(upload_to=settings.MEDIA_ROOT, max_length=100)
    site_url = models.URLField(max_length=200, null=True)
    
    slug = models.SlugField(max_length=50, unique=True)


    class Meta:
        db_table = 'project'


    def save(self, *args, **kwargs):
        if self.pk is None:
            try:
                self.slug = hashlib.sha1(os.urandom(50)).hexdigest()
            except IntegrityError as e:
                self.slug = hashlib.sha1(os.urandom(50)).hexdigest()
        self.screenshot = get_screenshot(self.site_url)
        to_return = super(Project, self).save(*args, **kwargs)
        
        return to_return


class ProjectFile(models.Model):
    """
    Links multiple files to a project
    """
    project_file_id = models.AutoField(primary_key=True)
    file = models.ForeignKey(File, null=True, on_delete=models.SET_NULL)
    project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'project_file'

from .tasks import get_screenshot
