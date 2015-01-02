import os, sys, re, shutil
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
    date_added = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(auto_now=False)
    team = models.CharField(max_length=255)
    screenshot = models.ImageField(upload_to=settings.MEDIA_ROOT, max_length=100)
    site_url = models.URLField(max_length=200, null=True)


    class Meta:
        db_table = 'project'


    def save(self, *args, **kwargs):
        try:
            self.screenshot = get_screenshot(self.site_url)
        except:
            pass

        to_return = super(Project, self).save(*args, **kwargs)
        return to_return


class ProjectFile(models.Model):
	"""
	Links multiple files to a project
	"""
	project_file_id = models.AutoField(primary_key=True)
	file = models.ForeignKey(File, null=True, on_delete=models.SET_NULL)
	project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)

#TODO: add bio, contact, blag, and other stuff
class Bio(models.Model):
    bio_id = models.AutoField(primary_key=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        db_table = 'bio'



from .tasks import get_screenshot
