# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 10:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DjgLeoApp001', '0003_auto_20170120_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='dates',
            name='doctorid',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, related_name='Doctor', to='DjgLeoApp001.People'),
            preserve_default=False,
        ),
    ]
