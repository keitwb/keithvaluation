# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-28 01:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keithvaluation', '0010_auto_20171126_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='property',
            name='longitude',
        ),
    ]
