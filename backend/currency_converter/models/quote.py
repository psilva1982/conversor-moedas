from django.db import models

from .money import Money


class Quote(Money):
    date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=3)
