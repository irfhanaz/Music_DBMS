# Generated by Django 3.2 on 2021-05-11 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='audio_url',
        ),
    ]
