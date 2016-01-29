from django.http import Http404
from django.db import connection
from django.shortcuts import render
from django.db.models import Sum, F
from hr_sales.models import SaleLog
import datetime
import json
import operator
import itertools


def format_date(x):
    x['date'] = x['date'].strftime('%a %Y-%m-%d')
    return x


def detail(request, year, month):
    truncate_date = connection.ops.date_trunc_sql('month', 'created')

    product_summary = SaleLog.objects.filter(
        date__year=year, date__month=month
    ).values('product').annotate(
        name=F('product__name'),
        quantity_sum=Sum('quantity'),
        profit=Sum(F('quantity')*F('price'))
    ).order_by('-product')

    date_summary = SaleLog.objects.filter(
        date__year=year, date__month=month
    ).values('date', 'product').annotate(
        quantity_sum=Sum('quantity'),
        profit=Sum(F('quantity')*F('price'))
    ).order_by('date')

    people_summary = SaleLog.objects.filter(
        date__year=year, date__month=month
    ).values('sale_man__name', 'product').annotate(
        quantity_sum=Sum('quantity'),
        profit=Sum(F('quantity')*F('price'))
    ).order_by('sale_man')

    date_summary = map(format_date, date_summary)

    available_product = [item['product'] for item in product_summary]

    date_collector = {
        'label': [],
        'qty': [],
        'profit': []
    }

    people_collector = {
        'label': [],
        'qty': [],
        'profit': []
    }

    for index, product in enumerate(available_product):
        date_collector['qty'].append([])
        date_collector['profit'].append([])
        people_collector['qty'].append([])
        people_collector['profit'].append([])

    for date, items in itertools.groupby(date_summary, key=operator.itemgetter('date')):
        # list_items = list(items)
        dict_items = dict([(item['product'], item) for item in items])

        date_collector['label'].append(date)

        for index, product in enumerate(available_product):
            date_collector['qty'][index].append(dict_items.get(product, {}).get('quantity_sum', 0))
            date_collector['profit'][index].append(dict_items.get(product, {}).get('profit', 0))

    for people, items in itertools.groupby(people_summary, key=operator.itemgetter('sale_man__name')):
        # list_items = list(items)
        dict_items = dict([(item['product'], item) for item in items])

        people_collector['label'].append(people)

        for index, product in enumerate(available_product):
            people_collector['qty'][index].append(dict_items.get(product, {}).get('quantity_sum', 0))
            people_collector['profit'][index].append(dict_items.get(product, {}).get('profit', 0))

    date_collector['qty'].append([sum(item) for item in zip(*date_collector['qty'])])
    date_collector['profit'].append([sum(item) for item in zip(*date_collector['profit'])])

    people_collector['qty'].append([sum(item) for item in zip(*people_collector['qty'])])
    people_collector['profit'].append([sum(item) for item in zip(*people_collector['profit'])])

    return render(request, 'hr_report/sale.html', {
        'product_summary': product_summary,
        'date_summary': date_summary,
        'available_product': available_product,
        'date_collector': json.dumps(date_collector),
        'people_collector': json.dumps(people_collector)
    })
