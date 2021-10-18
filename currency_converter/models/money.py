from django.db import models

SYMBOLS = ["BRL", "EUR", "JPY"]
SYMBOL_CHOICES = (
    (SYMBOLS[0], "Real"),
    (SYMBOLS[0], "Euro"),
    (SYMBOLS[0], "Iene"),
)


class Money(models.Model):
    symbol = models.CharField(max_length=3, choices=SYMBOL_CHOICES)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.symbol
