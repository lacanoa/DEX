# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-15 04:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dex', '0013_auto_20171014_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='SEC_UNDERLYING',
            field=models.CharField(default='NR', max_length=25),
        ),
    ]
