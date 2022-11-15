# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keithvaluation', '0003_auto_20151207_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='HuntingLease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('leased_to', models.CharField(help_text=b'Who the property is leased to', max_length=1024)),
                ('scanned_lease', models.FileField(help_text=b'Scanned PDF of the lease', null=True, upload_to=b'', blank=True)),
                ('lease_start_date', models.DateField(help_text=b'The start date of the lease')),
                ('lease_end_date', models.DateField(help_text=b'The end date of the lease')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('property_name', models.CharField(help_text=b'A short name for the property', max_length=256)),
                ('description', models.TextField(help_text=b'A longer description of the property.')),
                ('acreage', models.DecimalField(max_digits=8, decimal_places=1)),
                ('latitude', models.DecimalField(null=True, max_digits=9, decimal_places=6, blank=True)),
                ('longitude', models.DecimalField(null=True, max_digits=9, decimal_places=6, blank=True)),
                ('boundary_points', models.TextField(null=True, blank=True)),
                ('county', models.ForeignKey(to='keithvaluation.County', on_delete=models.DO_NOTHING)),
            ],
        ),
        migrations.AddField(
            model_name='huntinglease',
            name='property',
            field=models.ForeignKey(related_name='hunting_leases', to='keithvaluation.Property',
                                    on_delete=models.DO_NOTHING),
        ),
    ]
