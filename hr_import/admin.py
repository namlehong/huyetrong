from django.contrib import admin
from .models import ProductImport

# Register your models here.


class ProductImportAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'quantity', 'date', 'warehouse', 'created_at')
    readonly_fields = ('created_by',)

    def get_readonly_fields(self, request, obj=None):
        if not obj:
            return super(ProductImportAdmin, self).get_readonly_fields(request, obj)
        else:
            return ['created_by', 'product', 'price', 'quantity', 'warehouse', 'date']

    def save_model(self, request, obj, form, change):
        if not obj.created_by_id:
            obj.created_by_id = request.user.pk
        return super(ProductImportAdmin, self).save_model(request, obj, form, change)


admin.site.register(ProductImport, ProductImportAdmin)
