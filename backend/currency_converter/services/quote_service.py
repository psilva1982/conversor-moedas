import datetime as dt

from currency_converter.models.money import SYMBOLS
from currency_converter.models.quote import Quote
from rest_framework import serializers


def is_valid_symbol(symbol: str):

    if symbol not in SYMBOLS:
        raise serializers.ValidationError({"message": f"Moeda inválida, utilize {SYMBOLS}"})


def is_valid_date(date: str):
    try:
        year, month, day = date.split("-")
        dt.date(
            int(year),
            int(month),
            int(day),
        )
    except ValueError:
        raise serializers.ValidationError({"message": "Data inválida. Utilize o padrão YYYY-MM-DD"})


def is_valid_request(request):

    if "date" not in request.query_params.keys():
        raise serializers.ValidationError(
            {
                "message": "Data não informada",
                "field": "date",
            }
        )

    if "symbol" not in request.query_params.keys():
        raise serializers.ValidationError(
            {
                "message": "Moeda não informada",
                "field": "symbol",
            }
        )

    is_valid_date(request.query_params["date"])
    is_valid_symbol(request.query_params["symbol"])


def save_if_quote_not_exist(date: str, symbol: str, value: float) -> Quote:
    try:
        exist = Quote.objects.get(symbol=symbol, date=date)
        return exist
    except Quote.DoesNotExist:

        quote = Quote.objects.create(date=date, symbol=symbol, value=value)
        quote.save()

        return quote
