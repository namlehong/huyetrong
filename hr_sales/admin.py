from django.contrib import admin
from .models import SaleMan, SaleLog

# Register your models here.


class SaleLogAdmin(admin.ModelAdmin):
    list_display = ('sale_man', 'warehouse', 'date', 'product', 'quantity', 'price', 'created_at')
    readonly_fields = ('created_by',)

    def get_readonly_fields(self, request, obj=None):
        if not obj:
            return super(SaleLogAdmin, self).get_readonly_fields(request, obj)
        else:
            return ['sale_man', 'warehouse', 'product', 'quantity', 'price', 'created_at', 'created_by', 'note', 'date']

    def save_model(self, request, obj, form, change):
        if not obj.created_by_id:
            obj.created_by_id = request.user.pk
        return super(SaleLogAdmin, self).save_model(request, obj, form, change)


admin.site.register(SaleMan)
admin.site.register(SaleLog, SaleLogAdmin)
