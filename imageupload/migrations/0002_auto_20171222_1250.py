# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-22 07:20
from __future__ import unicode_literals

from django.db import migrations, models
import imageupload.models


class Migration(migrations.Migration):

    dependencies = [
        ('imageupload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage',
            name='image',
            field=models.ImageField(upload_to=imageupload.models.scramble_uploaded_filename, verbose_name='uploaded image'),
        ),
    ]
