from rest_framework import serializers

from currency_converter.models.quote import Quote


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ["symbol", "date", "value"]
