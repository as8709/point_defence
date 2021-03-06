# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-08 21:42
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Missile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design_name', models.CharField(max_length=200)),
                ('is_offensive', models.BooleanField()),
                ('fuel', models.PositiveSmallIntegerField()),
                ('thrust', models.PositiveIntegerField()),
                ('rotation_force', models.PositiveIntegerField()),
                ('radius', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('length', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('explosive_power', models.PositiveIntegerField()),
                ('script', models.TextField()),
                ('sensor_range', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('sensor_resolution', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('sensor_angle', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='MissileDesigns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='starter.Missile')),
            ],
        ),
    ]
