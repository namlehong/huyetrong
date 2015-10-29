from django.contrib import admin
from .models import Investment, Investor

# Register your models here.


class InvestorAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount')
    readonly_fields = ('amount',)


class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('investor', 'amount', 'created_at')
    readonly_fields = ('created_by',)

    def get_readonly_fields(self, request, obj=None):
        if not obj:
            return super(InvestmentAdmin, self).get_readonly_fields(request, obj)
        else:
            return ['created_by', 'investor', 'amount', 'warehouse', 'note', 'type']

    def save_model(self, request, obj, form, change):
        if not obj.created_by_id:
            obj.created_by_id = request.user.pk
        return super(InvestmentAdmin, self).save_model(request, obj, form, change)


admin.site.register(Investor, InvestorAdmin)
admin.site.register(Investment, InvestmentAdmin)
