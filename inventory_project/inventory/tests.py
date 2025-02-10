from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product

class ProductAPITest(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Laptop', stock=10)
    
    def test_create_product(self):
        response = self.client.post('/api/products/', {'name': 'Mouse', 'stock': 5}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_update_stock(self):
        response = self.client.patch(f'/api/products/{self.product.id}/', {'stock': 15}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 15)

    def test_delete_product(self):
        response = self.client.delete(f'/api/products/{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
