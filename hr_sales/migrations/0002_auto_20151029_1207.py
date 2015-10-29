# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr_sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salelog',
            name='note',
            field=models.TextField(null=True, blank=True),
        ),
    ]
