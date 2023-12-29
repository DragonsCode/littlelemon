from collections import OrderedDict
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="DontScream", price=50, inventory=200)
    
    def test_getall(self):
        url = reverse('menu-list')
        print("USED URL: ", url)
        client = APIClient()
        response = client.get(url, format='json')
        print(response.data)

        # Check if the request was successful (status code 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the expected data (adjust serializer based on your actual serializer)
        expected_data = [
            OrderedDict([('id', 2), ('title', 'IceCream'), ('price', '80.00'), ('inventory', 100)]),
            OrderedDict([('id', 3), ('title', 'DontScream'), ('price', '50.00'), ('inventory', 200)]),
        ]

        # Check if the serialized data equals the response data
        self.assertEqual(response.data, expected_data)