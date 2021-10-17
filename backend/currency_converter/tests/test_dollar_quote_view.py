from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class TestDollarQuoteViewSet(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_dollar_quotes_endpoint(self):
        """Test retrieving the dollar quote search"""
        url = reverse("dollar-quote-list") + "?date=2021-10-15&symbol=BRL"
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_dollar_with_out_query_params(self):
        """Test retrieving the dollar quote search"""
        url = reverse("dollar-quote-list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.data["message"], "Data não informada")
        self.assertEquals(response.data["field"], "date")

    def test_dollar_with_invalid_date(self):
        """Test retrieving the dollar quote search"""
        url = reverse("dollar-quote-list") + "?date=10-15-2021&symbol=BRL"
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.data["message"], "Data inválida. Utilize o padrão YYYY-MM-DD")

    def test_dollar_with_invalid_symbol(self):
        """Test retrieving the dollar quote search"""
        url = reverse("dollar-quote-list") + "?date=2021-10-15&symbol=RBL"
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.data["message"], "Moeda inválida, utilize ['BRL', 'EUR', 'JPY']")
