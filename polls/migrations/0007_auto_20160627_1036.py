# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20160627_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
