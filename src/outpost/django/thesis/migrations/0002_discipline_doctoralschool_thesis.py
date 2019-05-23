# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-08 09:47
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('thesis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('number', models.CharField(blank=True, max_length=256, null=True)),
                ('thesistype', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'thesis_discipline',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DoctoralSchool',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('emails', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(blank=True, max_length=254, null=True), size=None)),
            ],
            options={
                'db_table': 'thesis_doctoralschool',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('topic', models.CharField(blank=True, max_length=256, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('prerequisites', models.TextField(blank=True, null=True)),
                ('processstart', models.DateTimeField(blank=True, null=True)),
                ('goals', models.TextField(blank=True, null=True)),
                ('hypothesis', models.TextField(blank=True, null=True)),
                ('methods', models.TextField(blank=True, null=True)),
                ('schedule', models.TextField(blank=True, null=True)),
                ('milestones', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), size=None)),
            ],
            options={
                'db_table': 'thesis_thesis',
                'permissions': (('view_thesis', 'View thesis'),),
                'managed': False,
            },
        ),
    ]
