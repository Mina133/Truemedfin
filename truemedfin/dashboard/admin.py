from django.contrib import admin
from .models import *

class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "package", "number_of_pieces", "price_display")

    def price_display(self, obj):
        return f"${obj.price():.2f}"
    price_display.short_description = "Price"


class ListAdmin(admin.ModelAdmin):
    list_display = ("name", "list_price_display")

    def list_price_display(self, obj):
        return f"${obj.list_price():.2f}"
    list_price_display.short_description = "List Price"


class WorkingHoursAdmin(admin.ModelAdmin):
    list_display = ("hours_per_day", "days_per_week", "hours_per_week", "hours_per_month", "hours_per_year")


class DepreciationAdmin(admin.ModelAdmin):
    list_display = ("investment_cost", "number_of_years", "depreciation_per_year", "depreciation_per_month")


class FixedOperationalCoastAdmin(admin.ModelAdmin):
    list_display = (
        "rent",
        "routine_marketing",
        "bills",
        "secretary_and_assistant",
        "doctor_salaries",
        "fixed_operational_cost_per_month",
    )


class SpecializationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    filter_horizontal = ("specific_items", "specific_lists")


# Register your models
admin.site.register(Item, ItemAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(WorkingHours, WorkingHoursAdmin)
admin.site.register(Depreciation, DepreciationAdmin)
admin.site.register(FixedOperationalCost, FixedOperationalCoastAdmin)
admin.site.register(Specialization, SpecializationAdmin)
