# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-06 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_auto_20161206_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='publish_time',
            field=models.DateField(blank=True, null=True),
        ),
    ]