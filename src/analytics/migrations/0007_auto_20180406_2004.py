# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-06 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0006_auto_20180406_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productanalytic',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
