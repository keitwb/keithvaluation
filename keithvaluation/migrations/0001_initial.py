# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import keithvaluation.models.research


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BVResearch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('document', models.FileField(upload_to=keithvaluation.models.research.document_path)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated_date'],
                'abstract': False,
                'verbose_name_plural': 'Business Valuation Research',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourtCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('document', models.FileField(upload_to=keithvaluation.models.research.document_path)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated_date'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EconomicTrend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('document', models.FileField(upload_to=keithvaluation.models.research.document_path)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated_date'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExternalLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('date', models.DateField()),
            ],
            options={
                'ordering': ['-date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('document', models.FileField(upload_to=keithvaluation.models.research.document_path)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated_date'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='REResearch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('document', models.FileField(upload_to=keithvaluation.models.research.document_path)),
                ('updated_date', models.DateField(auto_now=True)),
                ('subtype', models.CharField(max_length=128, choices=[(b'Agricultural Properties', b'Agricultural Properties'), (b'Apartment', b'Apartment'), (b'Commercial', b'Commercial'), (b'Damage Studies', b'Damage Studies'), (b'Industrial', b'Industrial'), (b'Land Development', b'Land Development'), (b'Residential', b'Residential')])),
            ],
            options={
                'ordering': ['subtype', '-updated_date'],
                'verbose_name_plural': 'Real Estate Research',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=75)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=b'headshots')),
                ('resume', models.FileField(upload_to=b'resumes')),
                ('order', models.PositiveIntegerField(help_text=b'Relative ordering of this staff member (lowest is higher up on the page)')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name_plural': 'Staff',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WhitePaper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('document', models.FileField(upload_to=keithvaluation.models.research.document_path)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated_date'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
