# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=25)),
                ('product_unit', models.CharField(max_length=5)),
            ],
        ),
    ]
