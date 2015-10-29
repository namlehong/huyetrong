# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr_warehouse', '0001_initial'),
        ('hr_cook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cooksession',
            name='warehouse',
            field=models.ForeignKey(default=None, to='hr_warehouse.Warehouse'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cookingredient',
            name='product',
            field=models.ForeignKey(verbose_name=b'ingredient', to='hr_product.BaseProduct'),
        ),
    ]
