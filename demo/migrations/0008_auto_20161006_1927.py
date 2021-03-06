# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 18:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0030_index_on_pagerevision_created_at'),
        ('wagtaildocs', '0007_merge'),
        ('wagtailimages', '0015_fill_filter_spec_field'),
        ('demo', '0007_auto_20161006_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageGalleria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(blank=True, verbose_name='External link')),
                ('titolo', models.CharField(blank=True, max_length=55)),
                ('descrizione', models.CharField(blank=True, max_length=155)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('link_document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Pagina Principale Custom'},
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='body',
            new_name='campi_dinamici',
        ),
        migrations.AddField(
            model_name='homepage',
            name='secondo_titolo',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, verbose_name='Secondo Titolo Parallasse'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='titolo_principale',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, verbose_name='Titolo Parallasse'),
        ),
        migrations.AddField(
            model_name='homepagegalleria',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='galleria_home', to='demo.HomePage'),
        ),
    ]
