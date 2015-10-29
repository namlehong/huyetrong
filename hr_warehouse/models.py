from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
from hr_product.models import BaseProduct


class Warehouse(models.Model):
    name = models.CharField(max_length=200)
    is_root = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class WarehouseLog(models.Model):
    TYPE_IMPORT = 1
    TYPE_EXPORT = 2

    TYPE_CHOICES = (
        (TYPE_IMPORT, 'import'),
        (TYPE_EXPORT, 'export')
    )

    warehouse = models.ForeignKey(Warehouse)
    product = models.ForeignKey(BaseProduct)
    quantity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
