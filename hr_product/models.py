from django.db import models

# Create your models here.


class BaseProduct(models.Model):
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)

    def __unicode__(self):
        return u'{0} ({1})'.format(self.name, self.unit)
