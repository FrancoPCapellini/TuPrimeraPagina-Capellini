# Generated by Django 4.2.7 on 2023-12-14 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofile_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='owner',
        ),
    ]