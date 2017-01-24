# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0023_auto_20170123_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contestant',
            name='ans_array',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='current_que_id',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='first_login',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='que_array',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='score',
        ),
        migrations.AddField(
            model_name='usertest',
            name='ans_array',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='usertest',
            name='current_que_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='usertest',
            name='first_login',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usertest',
            name='que_array',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='usertest',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]