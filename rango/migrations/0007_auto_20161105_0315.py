# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-05 03:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20161105_0244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dimension',
            name='dim_id',
        ),
        migrations.RemoveField(
            model_name='metrics',
            name='metric_id',
        ),
        migrations.AddField(
            model_name='dimension',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 11, 5, 3, 15, 35, 412085, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimension',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 11, 5, 3, 15, 41, 991821, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
