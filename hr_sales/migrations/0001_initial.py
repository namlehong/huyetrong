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
            name='SaleLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField()),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(to='hr_product.BaseProduct')),
            ],
        ),
        migrations.CreateModel(
            name='SaleMan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='salelog',
            name='sale_man',
            field=models.ForeignKey(to='hr_sales.SaleMan'),
        ),
        migrations.AddField(
            model_name='salelog',
            name='warehouse',
            field=models.ForeignKey(to='hr_warehouse.Warehouse'),
        ),
    ]
