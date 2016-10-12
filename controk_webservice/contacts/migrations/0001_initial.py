# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('mobile', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Contact',
            },
        ),
    ]