from product import Product
from cart import ShoppingCart
import unittest

class ProductTestCase(unittest.TestCase):
    
    def setUp(self):
        # Method 1 -> Open class python script
        self.handle = open("product.py","r")
        # Method 2 -> Setup product variable 
        self.product = Product("Shoes","S","black")
        self.cart = ShoppingCart()
    
    def test_transform_name(self):
        expected_value = "SHOES"
        actual_value = self.product.transform_name_for_sku()
        self.assertEqual(expected_value,actual_value)
        
    def test_transform_color(self):
        expected_value = "BLACK"
        actual_value = self.product.transform_color_for_sku()
        self.assertEqual(expected_value,actual_value)
        
    def test_generate_sku(self):
        expected_value = "SHOES-S-BLACK"
        actual_value = self.product.generate_sku()
        self.assertEqual(expected_value,actual_value)
        
    def test_length(self):
        file_length = len(self.handle.readlines())
        self.assertTrue(file_length > 20)
        
    def test_cart_initially_empty(self):
        expected_value = {}
        self.assertDictEqual(expected_value,self.cart.products)
        
    def test_add_product(self):
        expected_value = {'SHOES-S-BLACK': {'quantity': 1}}
        self.cart.add_product(self.product)
        self.assertDictEqual(expected_value,self.cart.products)
        
    def test_add_two_of_a_product(self):
        expected_value = {'quantity': 2}
        self.cart.add_product(self.product,2)
        self.assertDictContainsSubset(expected_value,self.cart.products[self.product.generate_sku()])
        
    def tearDown(self):
        # Method 1 -> Close class python script
        self.handle.close()
        # Method 2 -> Delete product variable
        del self.product
        del self.cart
        
    # assertEqual(a, b)
    # assertNotEqual(a, b)
    # assertTrue(x)
    # assertFalse(x)
    # assertIsInstance(a, b)
    # assertIn(a, b)
    # assertAlmostEqual(a, b) like round(a-b, 7) == 0
    # assertGreaterEqual(a, b)
    # assertRegex(s, r) like r.search(s)
    # assertMultiLineEqual(a, b) compares two strings
    # assertDictEqual(a, b) compares two dictionaries
    # assertSequenceEqual(a, b) compares two sequences
            
        
unittest.main(argv =[""],verbosity= 2, exit= False)
