from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.conf import settings

# Create your models here.
from hr_cash.models import CashModifierAbstract, CashLog
from hr_warehouse.models import Warehouse


class Investor(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Investment(models.Model):
    TYPE_CASH = 1
    TYPE_CREDIT = 2

    TYPE_CHOICES = (
        (TYPE_CASH, 'cash'),
        (TYPE_CREDIT, 'credit')
    )

    investor = models.ForeignKey(Investor)
    type = models.IntegerField(choices=TYPE_CHOICES, default=TYPE_CREDIT)
    amount = models.IntegerField()
    warehouse = models.ForeignKey(Warehouse)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    note = models.TextField(blank=True, null=True)

    @staticmethod
    def nah_post_save(sender, instance, created, **kwargs):
        """

        :type instance: Investment
        """
        if created:
            if instance.type == Investment.TYPE_CASH:
                CashLog.objects.create(
                    content_object=instance,
                    warehouse=instance.warehouse,
                    amount=instance.amount
                )

            Investor.objects.filter(pk=instance.investor_id).update(amount=models.F('amount')+instance.amount)


models.signals.post_save.connect(Investment.nah_post_save, sender=Investment)
