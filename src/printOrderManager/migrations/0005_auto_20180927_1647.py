# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-27 22:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printOrderManager', '0004_auto_20180927_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printobject',
            name='advertisement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='printOrderManager.Advertisement'),
        ),
    ]
