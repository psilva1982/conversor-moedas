from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .factories import QuoteFactory


class TestQuotesViewSet(APITestCase):
    def setUp(self):
        self.client = APIClient()
        QuoteFactory.create_batch(15)

    def test_list_quotes_endpoint(self):
        """Test retrieving the list of quotes"""
        url = reverse("quote-list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data["count"], 15)

    def test_list_quotes_endpoint_with_pagination(self):
        """Test retrieving the list of quotes using pagination"""
        url = reverse("quote-list") + "?offset=10"
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data["count"], 15)
        self.assertEquals(len(response.data["results"]), 5)
