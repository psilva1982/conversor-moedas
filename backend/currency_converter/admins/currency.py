from currency_converter.models.currency import Currency
from django.contrib import admin


class SubjectAdmin(admin.ModelAdmin):
    search_fields = ["name"]


admin.site.register(Currency)
