# Generated by Django 3.0.8 on 2020-11-03 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_contact_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='status',
            new_name='read_status',
        ),
    ]
