from django.contrib import admin
from .models import CashLog

# Register your models here.


class CashLogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'warehouse', 'amount', 'created_at', 'content_type')
    readonly_fields = ('warehouse', 'amount', 'content_type', 'object_id')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

admin.site.register(CashLog, CashLogAdmin)
