from django.contrib import admin
from .models import CookSession, CookIngredient, CookProduct


# Register your models here.


class CookIngredientInline(admin.TabularInline):
    model = CookIngredient
    # readonly_fields = ('product', 'quantity')

    # def get_readonly_fields(self, request, obj=None):
    #     if obj:
    #         return 'product', 'quantity'
    #     else:
    #         return []


class CookProductInline(admin.TabularInline):
    model = CookProduct


class CookSessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'warehouse')
    readonly_fields = ('created_by',)
    inlines = [
        CookIngredientInline,
        CookProductInline
    ]

    def save_model(self, request, obj, form, change):
        if not obj.created_by_id:
            obj.created_by_id = request.user.pk
        return super(CookSessionAdmin, self).save_model(request, obj, form, change)


admin.site.register(CookSession, CookSessionAdmin)
