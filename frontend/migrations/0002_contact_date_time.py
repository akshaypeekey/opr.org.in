# Generated by Django 3.0.8 on 2020-10-19 19:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
