# Generated by Django 5.0.7 on 2024-07-13 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_remove_userprofile_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_profile_locked',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='state',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
    ]
