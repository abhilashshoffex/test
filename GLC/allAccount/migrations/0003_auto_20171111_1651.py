# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allAccount', '0002_auto_20171111_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coins',
            name='value',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='signup',
            name='referal_bonus',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='token',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='value',
            field=models.FloatField(),
        ),
    ]
