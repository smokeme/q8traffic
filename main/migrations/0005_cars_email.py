# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-18 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20171119_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='email',
            field=models.EmailField(default='q8fawazo@hotmail.com', max_length=340),
            preserve_default=False,
        ),
    ]