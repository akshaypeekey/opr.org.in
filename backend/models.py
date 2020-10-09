from django.db import models


# Create your models here.
class Index(models.Model):
    index_title = models.CharField(max_length=100)
    index_about_one = models.CharField(max_length=200)
    index_about_two = models.CharField(max_length=200)
    index_about_three = models.CharField(max_length=200)
    index_about_four = models.CharField(max_length=200)
    index_mission = models.CharField(max_length=200)
    index_event_one = models.CharField(max_length=200)
    index_event_two = models.CharField(max_length=200)
    index_event_three = models.CharField(max_length=200)

    def __str__(self):
        return self.index_title


class About(models.Model):
    about_title = models.CharField(max_length=100)
    about_us_one = models.CharField(max_length=200)
    about_us_two = models.CharField(max_length=200)
    about_number_one = models.IntegerField()
    about_number_two = models.IntegerField()
    about_number_three = models.IntegerField()
    about_number_four = models.IntegerField()
    about_sub_title = models.CharField(max_length=10)
    about_sub_para = models.CharField(max_length=200)
    about_sub_para_one = models.CharField(max_length=200)
    about_sub_para_two = models.CharField(max_length=200)
    about_sub_para_three = models.CharField(max_length=200)

    def __str__(self):
        return self.about_title


class Vision(models.Model):
    vision_title = models.CharField(max_length=10)
    vision_para_one = models.CharField(max_length=200)
    vision_para_two = models.CharField(max_length=200)
    mission_para_one = models.CharField(max_length=200)
    mission_para_two = models.CharField(max_length=200)
    mission_para_three = models.CharField(max_length=200)
    mission_para_four = models.CharField(max_length=200)
    download_cp = models.FileField()
    download_copr = models.FileField()
    manifesto_language = models.CharField(max_length=20)
    download_manifesto = models.FileField()

    def __str__(self):
        return self.vision_title


class Events(models.Model):
    events_title = models.CharField(max_length=120)
    events_para_one = models.CharField(max_length=200)
    events_para_two = models.CharField(max_length=200)
    events_para_three = models.CharField(max_length=200)
    events_para_four = models.CharField(max_length=200)

    def __str__(self):
        return self.events_title


class Contact(models.Model):
    contact_name = models.CharField(max_length=120)
    contact_email = models.EmailField()
    contact_subject = models.CharField(max_length=120)
    contact_message = models.CharField(max_length=120)

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
