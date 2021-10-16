from currency_converter.api.serializers.quote_serializers import QuoteSerializer
from currency_converter.selectors.quote_selectors import process_quotes
from currency_converter.services.quote_service import is_valid_request
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class DollarQuoteView(ViewSet):
    def list(self, request, format=None):

        is_valid_request(request)

        date = request.query_params["date"]
        symbol = request.query_params["symbol"]

        quotes = process_quotes(date, symbol)

        serializer = QuoteSerializer(quotes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
