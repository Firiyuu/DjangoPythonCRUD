# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 14:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('middle_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('course', models.CharField(max_length=250)),
                ('gender', models.CharField(max_length=250)),
                ('year', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects_taken', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Student')),
            ],
        ),
    ]
