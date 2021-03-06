# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('phonenumber', models.CharField(max_length=50)),
                ('service', models.CharField(choices=[('DATA', 'Data'), ('AIRTIME', 'Airtime'), ('AIRTIME 4 CASH', 'Airtime 4 Cash')], max_length=3)),
                ('complaint', models.TextField(max_length=500)),
                ('department', models.CharField(choices=[('BUSINESS', 'Business'), ('DESIGN', 'Design'), ('PAYPAL', 'PayPal')], max_length=3)),
            ],
        ),
    ]
