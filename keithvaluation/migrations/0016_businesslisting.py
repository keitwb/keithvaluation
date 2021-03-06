# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-04-15 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import keithvaluation.models.businesses


class Migration(migrations.Migration):

    dependencies = [
        ('keithvaluation', '0015_featureflag'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=512)),
                ('slug', models.SlugField()),
                ('subtitle', models.CharField(max_length=1024)),
                ('description', models.TextField()),
                ('flier', models.FileField(upload_to=keithvaluation.models.businesses.flier_path)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated_date'],
            },
        ),
    ]
