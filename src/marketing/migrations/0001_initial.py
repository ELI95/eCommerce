# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-24 13:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketingPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribed', models.BooleanField(default=True)),
                ('mailchimp_msg', models.TextField()),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
