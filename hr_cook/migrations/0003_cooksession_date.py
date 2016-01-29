# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hr_cook', '0002_auto_20151029_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='cooksession',
            name='date',
            field=models.DateField(default=datetime.date.today, null=True, blank=True),
        ),
    ]
