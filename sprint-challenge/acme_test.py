#!/usr/bin/env python
import unittest
from acme import Product
from acme_report import generate_products


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flammability(self):
        """Test default product flammability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_product_methods(self):
        """Test product methods stealability and explode."""
        prod = Product('Test Product')
        self.assertEqual(prod.stealability(), 'Kinda stealable')
        self.assertAlmostEqual(prod.explode(), '...boom!')


if __name__ == '__main__':
    unittest.main()