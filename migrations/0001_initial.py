# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-11 22:50
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('announcement_ID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('approved_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_management_announcement_approved_by', to=settings.AUTH_USER_MODEL)),
                ('requested_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_management_announcement_requested_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookConference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_meeting', models.CharField(blank=True, max_length=100, null=True, verbose_name='Meeting About')),
                ('requesting_date', models.DateField(blank=True, null=True, verbose_name='Requesting Date')),
                ('reason_for_room', models.CharField(choices=[(b'M', 'Meeting'), (b'T', 'Training'), (b'CM', 'Client Meeting')], max_length=15, verbose_name='Reason for room')),
                ('meeting_date', models.DateField(verbose_name='Meeting Date')),
                ('from_time', models.TimeField(blank=True, null=True, verbose_name='Meeting Start Time')),
                ('to_time', models.TimeField(blank=True, null=True, verbose_name='Meeting End Time')),
                ('no_of_persons', models.IntegerField(blank=True, null=True, verbose_name='No of Persons')),
                ('client_food_arrangement', models.CharField(blank=True, choices=[(b'S', 'Snacks'), (b'B', 'Breakfast'), (b'L', 'Lunch'), (b'D', 'Dinner')], max_length=15, null=True, verbose_name='Food Needed')),
                ('approved_date', models.DateField(blank=True, null=True, verbose_name='Approved Date')),
                ('attendence_needed', models.BooleanField(default=False, verbose_name='Attendance')),
                ('is_approved', models.BooleanField(default=False, verbose_name='is_approved')),
                ('is_approvedby', models.CharField(choices=[(b'Approve', b'Approve'), (b'Reject', b'Reject')], max_length=20, verbose_name='Approval Type')),
                ('approved_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name="{u'app_label': 'project_management', u'class': 'bookconference', u'model_name': 'bookconference'}(class)s_approved_by", to=settings.AUTH_USER_MODEL, verbose_name='Request To')),
            ],
            options={
                'verbose_name': 'Conference Room Booking',
                'verbose_name_plural': 'Conference Rooms Booking',
            },
        ),
        migrations.CreateModel(
            name='ConferenceRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=40)),
                ('no_of_seats', models.IntegerField(blank=True, null=True, verbose_name='No of seats')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='EquipmentsRequired',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='MeetingAttendees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conference_name', models.CharField(max_length=b'20')),
                ('attendees', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Conference Room Booking',
                'verbose_name_plural': 'Conference Rooms Booking',
            },
        ),
        migrations.AddField(
            model_name='conferenceroom',
            name='equipments_required',
            field=models.ManyToManyField(blank=True, null=True, to='project_management.EquipmentsRequired', verbose_name='Equipments'),
        ),
        migrations.AddField(
            model_name='bookconference',
            name='conference_room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="{u'app_label': 'project_management', u'class': 'bookconference', u'model_name': 'bookconference'}(class)s_conference_room", to='project_management.ConferenceRoom', verbose_name='Conference Room'),
        ),
        migrations.AddField(
            model_name='bookconference',
            name='equipments_required',
            field=models.ManyToManyField(blank=True, null=True, to='project_management.EquipmentsRequired', verbose_name='Equipments'),
        ),
        migrations.AddField(
            model_name='bookconference',
            name='requested_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name="{u'app_label': 'project_management', u'class': 'bookconference', u'model_name': 'bookconference'}(class)s_requested_by", to=settings.AUTH_USER_MODEL, verbose_name='Requested By'),
        ),
    ]
