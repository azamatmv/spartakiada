# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-19 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spartakiada', '0014_student_student_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='st_fac',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spartakiada.Faculty'),
        ),
    ]