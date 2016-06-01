# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management import call_command
from django.db import models, migrations

fixture = 'initial_data'

def load_fixture(apps, schema_editor):
    call_command('loaddata', fixture, app_label='keithvaluation')


class Migration(migrations.Migration):

    dependencies = [
        ('keithvaluation', '0004_county_huntinglease'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=lambda a, s: None),
    ]
