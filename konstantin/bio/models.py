from django.db import models

class Bio(models.Model):
    """
    Bio
    """
    bio_id = models.AutoField(primary_key=True)
    content = models.TextField()
    is_public = models.BooleanField()
