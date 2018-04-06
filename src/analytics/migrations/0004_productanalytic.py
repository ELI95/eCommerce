# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-06 19:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20180406_1547'),
        ('analytics', '0003_auto_20180404_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAnalytic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewed', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
