# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-22 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20171021_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.DeleteModel(
            name='Eyedb',
        ),
        migrations.DeleteModel(
            name='Hands',
        ),
        migrations.DeleteModel(
            name='Legs1',
        ),
        migrations.DeleteModel(
            name='Teethdb',
        ),
    ]