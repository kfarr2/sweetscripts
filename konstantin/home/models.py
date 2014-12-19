import os, sys
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models

class Admin(models.Model):
	admin_id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=255, unique=True)
	first_name = models.CharField(max_length=255, unique=True)
	last_name = models.CharField(max_length=255, unique=True)
	

	class Meta:
		db_table = "admin"

	def get_full_name(self): return self.last_name + ", " + self.first_name
	def get_short_name(self): return self.first_name + " " + self.last_name

	USERNAME_FIELD = 'username'

	objects = UserManager()


class About(models.Model):
    about_id = models.AutoField(primary_key=True)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "about"
        ordering = ['date_added']


class Dummy(models.Model):
    dummy_id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    tag = models.IntegerField()
    age = models.TimeField()
    created_by = models.ForeignKey(Admin)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "dummy"

