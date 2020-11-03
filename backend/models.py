from django.db import models


# Create your models here.
class Index(models.Model):
    index_title = models.CharField(max_length=100)
    index_about_one = models.CharField(max_length=1000)
    index_about_two = models.CharField(max_length=1000)
    index_about_three = models.CharField(max_length=1000)
    index_about_four = models.CharField(max_length=1000)
    index_mission_one = models.CharField(max_length=200, null=True, blank=True)
    index_mission_two = models.CharField(max_length=200, null=True, blank=True)
    index_mission_three = models.CharField(max_length=200, null=True, blank=True)
    index_mission_four = models.CharField(max_length=200, null=True, blank=True)
    index_mission_five = models.CharField(max_length=200, null=True, blank=True)
    index_mission_six = models.CharField(max_length=200, null=True, blank=True)
    index_mission_seven = models.CharField(max_length=200, null=True, blank=True)
    index_mission_eight = models.CharField(max_length=200, null=True, blank=True)
    index_mission_nine = models.CharField(max_length=200, null=True, blank=True)
    index_mission_ten = models.CharField(max_length=200, null=True, blank=True)
    index_event_one = models.CharField(max_length=200)
    index_event_two = models.CharField(max_length=200)
    index_event_three = models.CharField(max_length=200)

    def __str__(self):
        return self.index_title


class AboutUS(models.Model):
    about_title = models.CharField(max_length=10)
    about_us_one = models.CharField(max_length=1100)
    about_us_two = models.CharField(max_length=1000)
    about_number_one = models.IntegerField()
    about_number_two = models.IntegerField()
    about_number_three = models.IntegerField()
    about_number_four = models.IntegerField()
    about_sub_title = models.CharField(max_length=50)
    about_sub_para = models.CharField(max_length=500)
    about_sub_para_one = models.CharField(max_length=500)
    about_sub_para_two = models.CharField(max_length=500)
    about_sub_para_three = models.CharField(max_length=500)

    def __str__(self):
        return self.about_title


class VisionMission(models.Model):
    vision_title = models.CharField(max_length=10)
    vision_para_one = models.CharField(max_length=500)
    vision_para_two = models.CharField(max_length=500)
    mission_para_one = models.CharField(max_length=500)
    mission_para_two = models.CharField(max_length=500)
    mission_para_three = models.CharField(max_length=500)
    mission_para_four = models.CharField(max_length=500)
    download_cp = models.FileField()
    download_copr = models.FileField()
    manifesto_language = models.CharField(max_length=20)
    download_manifesto = models.FileField()

    def __str__(self):
        return self.vision_title


class Event(models.Model):
    events_title = models.CharField(max_length=10)
    events_para_one = models.CharField(max_length=1000)
    events_para_two = models.CharField(max_length=1000)
    events_para_three = models.CharField(max_length=1000)
    events_para_four = models.CharField(max_length=1000)

    def __str__(self):
        return self.events_title
