from  django.db import models
from django.contrib.auth.models import User
import uuid
from dataclasses import dataclass, Field





#User model
class USer(models.Model):
    firstname = models.CharField(max_length=200, null=True, db_index=True, blank=True)
    lastname = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200 , null=True)
    password = models.CharField(max_length=200, null=True)
    profile_pic = models.ForeignKey(Profile)

#Product model
class Product(models.Model):
    name = models.CharField(max_length=200, null=True, db_index=True, blank=True)
    lastname = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200 , null=True)
    password = models.CharField(max_length=200, null=True)
    profile_pic = models.ForeignKey(Profile)


#EMOTION model

#Live model