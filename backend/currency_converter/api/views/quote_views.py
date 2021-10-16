from currency_converter.api.serializers.quote_serializers import QuoteSerializer
from currency_converter.models.quote import Quote
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny


class QuoteView(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ["symbol"]
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [AllowAny]
    ordering = ["date"]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
