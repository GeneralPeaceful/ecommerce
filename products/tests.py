from django.test import TestCase
from .models import Product
# Create your tests here.
class ProductTest(TestCase):
    """Test various things relating to the Product model"""
    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name.name), 'A product')