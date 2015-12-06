# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keithvaluation', '0002_auto_20151003_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='resume',
            field=models.FileField(null=True, upload_to=b'resumes', blank=True),
        ),
    ]
