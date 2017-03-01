# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 07:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DjgLeoApp001', '0009_auto_20170222_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='bioexamination',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='BioExaminationCategories', to='DjgLeoApp001.ExaminationCategory', verbose_name='\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2'),
        ),
        migrations.AlterField(
            model_name='bioexamination',
            name='categorid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BioExaminationCategory', to='DjgLeoApp001.ExaminationCategory', verbose_name='\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1'),
        ),
        migrations.AlterField(
            model_name='examname',
            name='mm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DjgLeoApp001.MM', verbose_name='M\u03bf\u03bd\u03ac\u03b4\u03b1 M\u03ad\u03c4\u03c1\u03b7\u03c3\u03b7\u03c2(Min/Max)'),
        ),
        migrations.AlterField(
            model_name='examname',
            name='result_type',
            field=models.IntegerField(choices=[(1, '\u0391\u03c1\u03b9\u03b8\u03bc\u03b7\u03c4\u03b9\u03ba\u03cc'), (2, '\u039a\u03b5\u03af\u03bc\u03b5\u03bd\u03bf'), (3, '\u0391\u03c1\u03b9\u03b8\u03bc\u03b7\u03c4\u03b9\u03ba\u03cc + \u039a\u03b5\u03af\u03bc\u03b5\u03bd\u03bf'), (4, '\u0395\u03ba\u03c4\u03b5\u03bd\u03ad\u03c2 \u039a\u03b5\u03af\u03bc\u03b5\u03bd\u03bf'), (5, '\u039b\u03bf\u03b3\u03b9\u03ba\u03cc'), (9, '\u0386\u03bb\u03bb\u03bf')], max_length=1, verbose_name='\u0395\u03af\u03b4\u03bf\u03c2 \u0391\u03c0\u03ac\u03bd\u03c4\u03b7\u03c3\u03b7\u03c2'),
        ),
    ]
