from currency_converter.models.quote import Quote
from django.contrib import admin


class QuoteAdmin(admin.ModelAdmin):
    list_display = ["id", "date", "symbol", "value"]


admin.site.register(Quote, QuoteAdmin)
