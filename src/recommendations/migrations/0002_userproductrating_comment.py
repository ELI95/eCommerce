# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-08 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproductrating',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
