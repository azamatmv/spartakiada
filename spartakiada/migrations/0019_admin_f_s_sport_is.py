# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-04 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spartakiada', '0018_uchastniki_depart'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_f_s',
            name='sport_is',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spartakiada.Sport'),
        ),
    ]
