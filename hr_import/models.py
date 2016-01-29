from django.conf import settings
from django.db import models

# Create your models here.
from hr_product.models import BaseProduct
from hr_warehouse.models import WarehouseLog, Warehouse
from hr_cash.models import CashLog
import datetime


class ProductImport(models.Model):
    warehouse = models.ForeignKey(Warehouse)
    date = models.DateField(blank=True, null=True, default=datetime.date.today)
    product = models.ForeignKey(BaseProduct)
    price = models.IntegerField()
    quantity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    @staticmethod
    def post_save(sender, instance, created, **kwargs):
        """

        :type instance: ProductImport
        """
        if created:
            WarehouseLog.objects.create(
                content_object=instance,
                warehouse=instance.warehouse,
                product=instance.product,
                quantity=instance.quantity
            )

            CashLog.objects.create(
                content_object=instance,
                warehouse=instance.warehouse,
                amount=int(-instance.price * instance.quantity)
            )

models.signals.post_save.connect(ProductImport.post_save, sender=ProductImport)

