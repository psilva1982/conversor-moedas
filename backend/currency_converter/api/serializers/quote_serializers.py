from currency_converter.models.quote import Quote
from rest_framework import serializers


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ["symbol", "date", "value"]
