# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-09 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0007_club_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='asbaccountvalue',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='club',
            name='boostersaccountvalue',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='club',
            name='grantaccountvalue',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
