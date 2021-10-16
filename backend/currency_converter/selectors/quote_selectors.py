import datetime as dt
from json.decoder import JSONDecodeError

import requests
from currency_converter.services.quote_service import save_if_quote_not_exist
from django.conf import settings


def get_last_util_days(date: str, number_of_days: int) -> list:

    year, month, day = date.split("-")
    date_select = dt.date(int(year), int(month), int(day))
    dates = []
    count = 0

    while len(dates) < number_of_days:
        temp_date = dt.date.fromordinal(date_select.toordinal() - count)

        # 5 - saturday // 6 - sunday
        # if the weekday is between 0 and 4 it will be a working day
        if temp_date.weekday() < 5:
            dates.append(str(temp_date))

        count += 1

    return dates


def get_dollar_quote(date: str, symbol: str) -> float:
    try:
        req = requests.get(f"{settings.VAT_COMPLY_URL}?date={date}")

        dolar_quote = req.json()["rates"]["USD"]
        symbol_quote = req.json()["rates"][symbol]

        return symbol_quote / dolar_quote

    except JSONDecodeError:
        return 0


def process_quotes(date: str, symbol: str):

    dates = get_last_util_days(date, number_of_days=5)
    quotes = []
    for date in dates:
        value = get_dollar_quote(date, symbol)

        if value != 0:
            quote = save_if_quote_not_exist(date=date, symbol=symbol, value=value)
            quotes.append(quote)

    return quotes
