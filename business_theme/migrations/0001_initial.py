# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-28 08:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('pages', '0004_auto_20170411_0504'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('heading', models.CharField(default='Hello, world!', help_text='The heading under the icon blurbs', max_length=200, verbose_name='Heading')),
                ('subheading', models.CharField(default='This is a template for a simple marketing or informational website. It includes a large callout called a jumbotron and three supporting pieces of content. Use it as a starting point to create something more unique.', help_text='The subheading just below the heading', max_length=1000, verbose_name='Subheading')),
                ('heading_button', models.CharField(default='Learn more', max_length=200, verbose_name='Button text')),
                ('heading_link', models.CharField(blank=True, default='#', help_text='Optional, if provided the heading button will be visible.', max_length=200, verbose_name='Button link')),
                ('iconbox_heading', models.CharField(blank=True, help_text='Optional, if provided the iconbox heading will be visible.', max_length=200, null=True, verbose_name='Iconbox heading')),
                ('content_heading', models.CharField(default='About us', max_length=200, verbose_name='Content heading')),
            ],
            options={
                'verbose_name': 'Home page',
                'verbose_name_plural': 'Home pages',
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='IconBlurb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('icon', mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='Image')),
                ('title', models.CharField(default='Heading', max_length=200, verbose_name='Title')),
                ('content', models.TextField(default='Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.', verbose_name='Content')),
                ('link', models.CharField(blank=True, help_text='Optional, if provided clicking the blurb will go here.', max_length=2000, verbose_name='Link')),
                ('homepage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blurbs', to='business_theme.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='SitewideContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_one_title', models.CharField(default='About', max_length=200, verbose_name='Box 1 title')),
                ('box_one_content', mezzanine.core.fields.RichTextField(default='Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.', verbose_name='Box 1 content')),
                ('box_two_title', models.CharField(default='Contact Us', max_length=200, verbose_name='Box 2 title')),
                ('box_two_content', mezzanine.core.fields.RichTextField(default='Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.', verbose_name='Box 2 content')),
                ('box_three_title', models.CharField(default='Social links', max_length=200, verbose_name='Box 3 title')),
                ('box_three_content', mezzanine.core.fields.RichTextField(default='Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.', verbose_name='Box 3 content')),
                ('site', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name': 'Sitewide Content',
                'verbose_name_plural': 'Sitewide Content',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('image', mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='Image')),
                ('homepage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slides', to='business_theme.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
    ]
