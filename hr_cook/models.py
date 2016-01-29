from django.db import models
from django.conf import settings
from hr_product.models import BaseProduct
from hr_warehouse.models import Warehouse, WarehouseLog
import datetime
# Create your models here.


class CookSession(models.Model):
    name = models.CharField(max_length=200)
    warehouse = models.ForeignKey(Warehouse)
    date = models.DateField(blank=True, null=True, default=datetime.date.today)
    create_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)


class CookIngredient(models.Model):
    product = models.ForeignKey(BaseProduct, verbose_name='ingredient')
    cook_session = models.ForeignKey(CookSession, related_name='ingredients')
    quantity = models.FloatField()

    @staticmethod
    def post_save(sender, instance, created, **kwargs):
        if created:
            WarehouseLog.objects.create(
                content_object=instance.cook_session,
                warehouse=instance.cook_session.warehouse,
                product=instance.product,
                quantity=-instance.quantity
            )


class CookProduct(models.Model):
    product = models.ForeignKey(BaseProduct)
    cook_session = models.ForeignKey(CookSession, related_name='products')
    quantity = models.FloatField()

    @staticmethod
    def post_save(sender, instance, created, **kwargs):
        if created:
            WarehouseLog.objects.create(
                content_object=instance.cook_session,
                warehouse=instance.cook_session.warehouse,
                product=instance.product,
                quantity=instance.quantity
            )


models.signals.post_save.connect(CookProduct.post_save, sender=CookProduct)
models.signals.post_save.connect(CookIngredient.post_save, sender=CookIngredient)
