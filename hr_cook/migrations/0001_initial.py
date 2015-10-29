# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hr_product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookIngredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CookProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CookSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cookproduct',
            name='cook_session',
            field=models.ForeignKey(related_name='products', to='hr_cook.CookSession'),
        ),
        migrations.AddField(
            model_name='cookproduct',
            name='product',
            field=models.ForeignKey(to='hr_product.BaseProduct'),
        ),
        migrations.AddField(
            model_name='cookingredient',
            name='cook_session',
            field=models.ForeignKey(related_name='ingredients', to='hr_cook.CookSession'),
        ),
        migrations.AddField(
            model_name='cookingredient',
            name='product',
            field=models.ForeignKey(to='hr_product.BaseProduct'),
        ),
    ]
