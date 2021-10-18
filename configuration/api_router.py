from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from currency_converter.api.views.dollar_quote_view import DollarQuoteView
from currency_converter.api.views.quote_views import QuoteView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r"quotes", QuoteView)
router.register(r"dollar-quote", DollarQuoteView, basename="dollar-quote")

urlpatterns = router.urls
