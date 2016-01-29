from django.db import models
from django.conf import settings

from hr_cash.models import CashLog
from hr_product.models import BaseProduct
from hr_warehouse.models import Warehouse, WarehouseLog

# Create your models here.


class SaleMan(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


import datetime


class SaleLog(models.Model):
    sale_man = models.ForeignKey(SaleMan)
    warehouse = models.ForeignKey(Warehouse)
    date = models.DateField(blank=True, null=True, default=datetime.date.today)
    product = models.ForeignKey(BaseProduct)
    quantity = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    note = models.TextField(blank=True, null=True)

    @staticmethod
    def post_save(sender, instance, created, **kwargs):
        """

        :type instance: SaleLog
        """
        if created:
            CashLog.objects.create(
                content_object=instance,
                warehouse=instance.warehouse,
                amount=instance.price*instance.quantity
            )
            
            WarehouseLog.objects.create(
                content_object=instance,
                warehouse=instance.warehouse,
                product=instance.product,
                quantity=-instance.quantity
            )


models.signals.post_save.connect(SaleLog.post_save, sender=SaleLog)
