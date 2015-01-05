from django.db import models

# Create your models here.
class BlogPost(models.Model):
    """
    General model for a blog post.
    """
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    allow_comments = models.BooleanField(default=True)

    class Meta:
        db_table = 'blog'

