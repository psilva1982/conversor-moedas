import datetime as dt

from factory import fuzzy
from factory.django import DjangoModelFactory

from currency_converter.models.quote import Quote


class QuoteFactory(DjangoModelFactory):

    symbol = "BRL"
    value = fuzzy.FuzzyDecimal(0, 200)
    date = fuzzy.FuzzyDate(dt.date(2010, 1, 1), dt.date(2021, 10, 15))

    class Meta:
        model = Quote
