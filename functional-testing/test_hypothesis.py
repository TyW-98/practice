from hypothesis import given, assume
from hypothesis_element import decode, encode, even
from math import isnan
import hypothesis.strategies as st
import unittest

class Test_encoder(unittest.TestCase):
    @given(st.text())
    
    def test_decoder(self, s):
        self.assertEqual(decode(encode(s)),s)
        
    # Filters out the odd numbers  
    @given(st.integers().filter(lambda x: x % 2 ==0))
    def test_even_integers(self,i):
        self.assertEqual(even(i),True)
        
    # Assume input is/ is not something
    @given(st.floats())
    def test_negation_is_self_inverse_for_non_nan(self,x):
        assume(not isnan(x))
        assert x == -(-x)
    
        
unittest.main(argv= [""], verbosity=2, exit= False) 

