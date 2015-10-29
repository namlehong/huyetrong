# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr_cash', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directcash',
            name='note',
            field=models.TextField(null=True, blank=True),
        ),
    ]
