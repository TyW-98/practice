from product import Product
import unittest

class ProductTestCase(unittest.TestCase):
    
    def setUp(self):
        # Method 1 -> Open class python script
        self.handle = open("product.py","r")
        # Method 2 -> Setup product variable 
        self.product = Product("Shoes","S","black")
    
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
        
    def tearDown(self):
        # Method 1 -> Close class python script
        self.handle.close()
        # Method 2 -> Delete product variable
        del self.product
        
        
unittest.main(argv =[""],verbosity= 2, exit= False)
