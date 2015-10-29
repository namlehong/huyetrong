from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

# Create your models here.
from hr_warehouse.models import Warehouse


class CashLog(models.Model):
    warehouse = models.ForeignKey(Warehouse)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class CashModifierAbstract(models.Model):
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    note = models.TextField(blank=True, null=True)
    # logs = GenericRelation(CashLog)

    class Meta:
        abstract = True

    @staticmethod
    def post_save(sender, instance, created, **kwargs):
        """
        :type instance: Investment
        """
        if created:
            CashLog.objects.get_or_create(
                content_object=instance,
                defaults={
                    'warehouse': Warehouse.objects.filter(is_root=True)[0],
                    'amount': instance.amount
                }
            )


class DirectCash(CashModifierAbstract):
    pass


models.signals.post_save.connect(DirectCash.post_save, sender=DirectCash)
