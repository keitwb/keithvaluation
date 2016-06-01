# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keithvaluation', '0005_auto_20160511_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='huntinglease',
            name='latitude',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=6, blank=True),
        ),
        migrations.AddField(
            model_name='huntinglease',
            name='longitude',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=6, blank=True),
        ),
    ]
