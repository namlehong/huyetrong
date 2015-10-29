# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('hr_warehouse', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hr_product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.IntegerField()),
                ('quantity', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(to='hr_product.BaseProduct')),
                ('warehouse', models.ForeignKey(to='hr_warehouse.Warehouse')),
            ],
        ),
    ]
