from product import Product
from cart import ShoppingCart
import unittest

class ShoppingCartTestCase(unittest.TestCase):
    
    def setUp(self):
        self.cart = ShoppingCart()
        self.item = Product("Shoes","S","black")
        
    def test_add_and_remove_product(self):
        self.cart.add_product(self.item)
        self.cart.remove_product(self.item)
        self.assertDictEqual({},self.cart.products)
        

unittest.main(argv = [""], verbosity= 3, exit = False)
        
        