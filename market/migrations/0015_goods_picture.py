# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-20 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0014_auto_20161208_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='goods'),
        ),
    ]