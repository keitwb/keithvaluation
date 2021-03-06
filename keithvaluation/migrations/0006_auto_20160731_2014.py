# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('keithvaluation', '0005_auto_20160729_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeasedProperty',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'leased properties',
            },
            bases=('keithvaluation.property',),
        ),
        migrations.AddField(
            model_name='property',
            name='aerial_photo',
            field=models.ImageField(blank=True, null=True, upload_to=b'aerial-photos'),
        ),
        migrations.AlterField(
            model_name='huntinglease',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hunting_leases', to='keithvaluation.LeasedProperty'),
        ),
    ]
