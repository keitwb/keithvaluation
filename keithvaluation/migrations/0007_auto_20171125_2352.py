# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-25 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keithvaluation', '0006_auto_20160731_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='state',
            field=models.CharField(choices=[[b'NC', b'NC']], default='NC', max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='county',
            field=models.CharField(max_length=256),
        ),
        migrations.DeleteModel(
            name='County',
        ),
    ]
