# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vranaya_app', '0010_video_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='view_counter',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='song',
            name='view_counter',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='video',
            name='video_logo',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='video',
            name='view_counter',
            field=models.IntegerField(default=1),
        ),
    ]
