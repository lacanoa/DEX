# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-08 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dex', '0008_tradeaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradeaccount',
            name='NAME',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
