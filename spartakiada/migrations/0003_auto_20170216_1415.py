# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-16 14:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spartakiada', '0002_auto_20170216_1414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_numner',
            new_name='student_number',
        ),
    ]
