# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0030_index_on_pagerevision_created_at'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtaildocs', '0007_merge'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailsearchpromotions', '0002_capitalizeverbose'),
        ('demo', '0014_auto_20161006_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventIndexPageLinkEsterno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(blank=True, verbose_name='External link')),
                ('title', models.CharField(help_text='Link title', max_length=255)),
                ('link_document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='link_esterno', to='demo.EventIndexPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='eventpagecarouselitem',
            name='image',
        ),
        migrations.RemoveField(
            model_name='eventpagecarouselitem',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='eventpagecarouselitem',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='eventpagecarouselitem',
            name='page',
        ),
        migrations.RemoveField(
            model_name='eventpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='eventpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='eventpagerelatedlink',
            name='page',
        ),
        migrations.RemoveField(
            model_name='eventpagespeaker',
            name='image',
        ),
        migrations.RemoveField(
            model_name='eventpagespeaker',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='eventpagespeaker',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='eventpagespeaker',
            name='page',
        ),
        migrations.DeleteModel(
            name='EventPage',
        ),
        migrations.DeleteModel(
            name='EventPageCarouselItem',
        ),
        migrations.DeleteModel(
            name='EventPageRelatedLink',
        ),
        migrations.DeleteModel(
            name='EventPageSpeaker',
        ),
    ]