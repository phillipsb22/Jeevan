# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-29 06:15
from __future__ import unicode_literals

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20171029_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, keep_meta=True, quality=0, size=[300, 300], upload_to='products/%Y/%m/%d'),
        ),
    ]