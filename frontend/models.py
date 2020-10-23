from django.db import models

# Create your models here.
from datetime import datetime


class Contact(models.Model):
    contact_name = models.CharField(max_length=120)
    contact_email = models.EmailField()
    contact_subject = models.CharField(max_length=120)
    contact_message = models.TextField()
    date_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.contact_name


class Member(models.Model):
    name = models.CharField(max_length=120)
    residential_address = models.CharField(max_length=120)
    district = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    pin = models.IntegerField()
    phone = models.IntegerField()
    age = models.CharField(max_length=120)

    def __str__(self):
        return self.name