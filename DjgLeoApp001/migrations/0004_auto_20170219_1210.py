# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DjgLeoApp001', '0003_auto_20170219_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bioexaminationdetail',
            name='notes',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='\u03a3\u03b7\u03bc\u03b5\u03b9\u03ce\u03c3\u03b5\u03b9\u03c2'),
        ),
        migrations.AlterField(
            model_name='examschema',
            name='notes',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='\u03a3\u03b7\u03bc\u03b5\u03b9\u03ce\u03c3\u03b5\u03b9\u03c2'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='categorid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjgLeoApp001.MedicineCategory', verbose_name='\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='dateend',
            field=models.DateField(verbose_name='\u0388\u03c9\u03c2'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='dateof',
            field=models.DateField(verbose_name='\u0397\u03bc\u03b5\u03c1\u03bf\u03bc\u03b7\u03bd\u03af\u03b1'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='datestart',
            field=models.DateField(verbose_name='\u0391\u03c0\u03cc'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='doctorid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MedicineDoctor', to='DjgLeoApp001.People', verbose_name='\u0393\u03b9\u03b1\u03c4\u03c1\u03cc\u03c2'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='notes',
            field=models.CharField(blank=True, max_length=8192, null=True, verbose_name='\u03a3\u03b7\u03bc\u03b5\u03b9\u03ce\u03c3\u03b5\u03b9\u03c2'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='peopleid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjgLeoApp001.People', verbose_name='\u0391\u03c3\u03b8\u03b5\u03bd\u03ae\u03c2'),
        ),
        migrations.AlterField(
            model_name='operations',
            name='categorid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjgLeoApp001.OperationCategory', verbose_name='\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1'),
        ),
        migrations.AlterField(
            model_name='operations',
            name='comments',
            field=models.CharField(blank=True, max_length=8192, null=True, verbose_name='\u03a3\u03c7\u03cc\u03bb\u03b9\u03b1'),
        ),
        migrations.AlterField(
            model_name='operations',
            name='dateof',
            field=models.DateField(verbose_name='\u0397\u03bc\u03b5\u03c1\u03bf\u03bc\u03b7\u03bd\u03af\u03b1'),
        ),
        migrations.AlterField(
            model_name='operations',
            name='doctorid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OperationDoctor', to='DjgLeoApp001.People', verbose_name='\u0393\u03b9\u03b1\u03c4\u03c1\u03cc\u03c2'),
        ),
        migrations.AlterField(
            model_name='operations',
            name='notes',
            field=models.CharField(blank=True, max_length=8192, null=True, verbose_name='\u03a3\u03b7\u03bc\u03b5\u03b9\u03ce\u03c3\u03b5\u03b9\u03c2'),
        ),
        migrations.AlterField(
            model_name='operations',
            name='peopleid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjgLeoApp001.People', verbose_name='\u0391\u03c3\u03b8\u03b5\u03bd\u03ae\u03c2'),
        ),
        migrations.AlterField(
            model_name='people',
            name='notes',
            field=models.CharField(blank=True, max_length=8192, null=True, verbose_name='\u03a3\u03b7\u03bc\u03b5\u03b9\u03ce\u03c3\u03b5\u03b9\u03c2'),
        ),
        migrations.AlterField(
            model_name='specialusers',
            name='notes',
            field=models.CharField(max_length=100, verbose_name='\u03a3\u03b7\u03bc\u03b5\u03b9\u03ce\u03c3\u03b5\u03b9\u03c2'),
        ),
    ]
