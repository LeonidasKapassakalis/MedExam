# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 12:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DjgLeoApp001', '0011_auto_20170224_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamSchemaDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'ordering': ('ExamSchema', 'ExamName'),
            },
        ),
        migrations.AlterField(
            model_name='examname',
            name='mm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DjgLeoApp001.MM', verbose_name='M\u03bf\u03bd\u03ac\u03b4\u03b1 M\u03ad\u03c4\u03c1\u03b7\u03c3\u03b7\u03c2(Min/Max)'),
        ),
        migrations.AddField(
            model_name='examschemadetail',
            name='ExamName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjgLeoApp001.Examname', verbose_name='\u0395\u03be\u03ad\u03c4\u03b1\u03c3\u03b7'),
        ),
        migrations.AddField(
            model_name='examschemadetail',
            name='ExamSchema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjgLeoApp001.Examschema', verbose_name='\u03a3\u03c7\u03ae\u03bc\u03b1'),
        ),
        migrations.AlterUniqueTogether(
            name='examschemadetail',
            unique_together=set([('ExamSchema', 'ExamName')]),
        ),
    ]
