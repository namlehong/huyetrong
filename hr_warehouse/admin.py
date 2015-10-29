from django.contrib import admin
from .models import Warehouse, WarehouseLog

# Register your models here.


class WarehouseLogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'warehouse', 'product', 'quantity', 'created_at')
    readonly_fields = ('warehouse', 'product', 'quantity', 'content_type', 'object_id')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(Warehouse)
admin.site.register(WarehouseLog, WarehouseLogAdmin)
