# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-11 22:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('type', models.CharField(blank=True, max_length=120, null=True, verbose_name='event type')),
                ('date', models.DateField(verbose_name='date')),
                ('start_time', models.TimeField(verbose_name='start Time')),
                ('end_time', models.TimeField(verbose_name='end Time')),
                ('venue', models.CharField(blank=True, max_length=120, null=True, verbose_name='venue')),
                ('location', models.CharField(blank=True, max_length=120, null=True, verbose_name='location')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('cancel', models.BooleanField(default=False, verbose_name='cancel')),
                ('attendees', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='attendees')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications_event_development_process', to=settings.AUTH_USER_MODEL, verbose_name='creator')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='project')),
            ],
        ),
    ]