# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='department',
            field=models.CharField(choices=[('BUSINESS', 'Business'), ('DESIGN', 'Design'), ('PAYPAL', 'PayPal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='service',
            field=models.CharField(choices=[('DATA', 'Data'), ('AIRTIME', 'Airtime'), ('AIRTIME 4 CASH', 'Airtime 4 Cash')], max_length=50),
        ),
    ]
