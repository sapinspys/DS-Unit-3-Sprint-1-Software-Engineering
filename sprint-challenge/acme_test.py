#!/usr/bin/env python
import unittest
from acme import Product
from acme_report import generate_products, adj, noun, inventory_report

import io
import sys


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
        self.assertEqual(prod.explode(), '...boom!')


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        """Test number of products generated by default."""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """Tests that the generated product names are all valid possible names."""
        products = generate_products()
        for product in products:
            x = product.name.split(" ")
            self.assertIn(x[0], adj)
            self.assertIn(x[1], noun)

    # STRETCH, for inventory_report()
    def test_inventory_report(self):
        """Tests that the inventory report summary is correct."""
        products = [Product('test1'), Product('test1', 20, 40, 1)]
        final_value = 'ACME CORPORATION OFFICIAL INVENTORY REPORT\nUnique product names: 1\nAverage price: 15\nAverage weight: 30\nAverage flammability: 0.75\n'

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        inventory_report(products)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), final_value)


if __name__ == '__main__':
    unittest.main()
