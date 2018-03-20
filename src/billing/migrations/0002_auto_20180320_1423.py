# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-20 14:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', models.CharField(max_length=120)),
                ('brand', models.CharField(blank=True, max_length=120, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('exp_month', models.IntegerField(blank=True, null=True)),
                ('exp_year', models.IntegerField(blank=True, null=True)),
                ('last4', models.CharField(blank=True, max_length=4, null=True)),
                ('default', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', models.CharField(max_length=120)),
                ('paid', models.BooleanField(default=False)),
                ('refunded', models.BooleanField(default=False)),
                ('outcome', models.TextField(blank=True, null=True)),
                ('outcome_type', models.CharField(blank=True, max_length=120, null=True)),
                ('seller_message', models.CharField(blank=True, max_length=120, null=True)),
                ('risk_level', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='billingprofile',
            name='customer_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='charge',
            name='billing_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.BillingProfile'),
        ),
        migrations.AddField(
            model_name='card',
            name='billing_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.BillingProfile'),
        ),
    ]
