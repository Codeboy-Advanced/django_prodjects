# Generated by Django 5.1.5 on 2025-02-25 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Culinary', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reser',
            old_name='time',
            new_name='t',
        ),
        migrations.RenameField(
            model_name='timeslot',
            old_name='time',
            new_name='t',
        ),
    ]
