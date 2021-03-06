# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 12:24
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0005_auto_20161226_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Listed'), (1, 'Pending'), (2, 'Sold')], null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='owner',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='realestate.Tag'),
        ),
        migrations.AlterField(
            model_name='property_promo',
            name='header',
            field=cloudinary.models.CloudinaryField(blank=True, help_text='Upload header image for brand', max_length=255, null=True, verbose_name='promo'),
        ),
    ]
