from django.db import models

class Bio(models.Model):
    """
    Bio
    """
    bio_id = models.AutoField(primary_key=True)
    content = models.TextField()
    is_public = models.BooleanField(default=False)

    class Meta:
        db_table = "bio"


class Contact(models.Model):
    """
    Contact
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

    

    class Meta:
        db_table = "contact"
