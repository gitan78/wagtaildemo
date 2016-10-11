# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-07 19:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0015_fill_filter_spec_field'),
        ('demo', '0022_auto_20161007_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='avatar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]