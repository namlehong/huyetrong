# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hr_import', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimport',
            name='date',
            field=models.DateField(default=datetime.date.today, null=True, blank=True),
        ),
    ]
