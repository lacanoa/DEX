# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-14 03:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dex', '0012_position_ordergroup'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='position',
            unique_together=set([('TRDACCID', 'SECCODE')]),
        ),
    ]
