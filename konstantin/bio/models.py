from django.db import models

class Bio(models.Model):
    """
    Bio - Technically the "about" section on the actual site.

    """
    bio_id = models.AutoField(primary_key=True)
    content = models.TextField()
    is_public = models.BooleanField(default=False)
    avatar = models.ImageField(null=True)

    class Meta:
        db_table = "bio"


class Contact(models.Model):
    """
    Contact - Contact data. Some of which will be used in the resume section.

    """
    # DB stuff
    contact_id = models.AutoField(primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)

    # Name Stuff
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

    # DOB
    birthday = models.DateField()

    # Address
    address = models.CharField(max_length=255)


    class Meta:
        db_table = "contact"

"""
Should probably add a resume section around here.

"""
