# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_invoice_invoicepayment_pendinginvoicepayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicepayment',
            name='is_old_adress',
            field=models.BooleanField(default=False),
        ),
    ]