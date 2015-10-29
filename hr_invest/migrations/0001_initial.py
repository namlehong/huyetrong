# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('hr_warehouse', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(default=2, choices=[(1, b'cash'), (2, b'credit')])),
                ('amount', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(null=True, blank=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='investment',
            name='investor',
            field=models.ForeignKey(to='hr_invest.Investor'),
        ),
        migrations.AddField(
            model_name='investment',
            name='warehouse',
            field=models.ForeignKey(to='hr_warehouse.Warehouse'),
        ),
    ]
