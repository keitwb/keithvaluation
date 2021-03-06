# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-28 02:53
from __future__ import unicode_literals

from django.db import migrations, models
import keithvaluation.models.research


class Migration(migrations.Migration):

    dependencies = [
        ('keithvaluation', '0011_auto_20171128_0142'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpertTestimony',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('document', models.FileField(upload_to=keithvaluation.models.research.document_path)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'expert testimonies',
            },
        ),
    ]
