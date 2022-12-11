""" 
This is the temperature module.
"""

from dataclasses import dataclass

@dataclass(order=True)
class temperature:
    """The temperature converter
    
    This class uses the dataclass from dataclasses to create the class and it comes with the __init__,
    __repr__ and __eq__ methods.
    
    Attributes:
        temp (int): The temeperature value 
    """
    temp: int
    
    @property
    def temp(self):
        print(f"The temperature is {self.__temp}")
        return self.__temp
    
    @temp.setter
    def temp(self,temp):
        print("Storing temperature value")
        self.__temp = temp
        
    @temp.deleter
    def temp(self):
        print("Deleting temperature value")
        del self.__temp
        
    def temp_fahrenheit(self):
        """ Converts temperature to fahrenheit
        
        Takes in temperature in celsius and converts it to fahrenheit
        
        Returns:
            int: the return value of the temperature in fahrenheit
        
        """
        fahrenheit = (self.__temp*(9/5))+ 32
        return fahrenheit
    
    @staticmethod
    def temp_celsius(temp):
        """ Converts temperature to celsius
        
        Takes in the temperature in fahrenheit and converts it to celsius.
        
        Args:
            temp (int): the value of the temperature in fahrenheit.
            
        Returns:
            int: return the value of the temperature in celsius.
        """
        celsius = (int(temp)-32)*(5/9)
        return celsius
        
    @staticmethod
    def temp_checker(temp):
        """Check if temperature is within range
        
        Check if the temperature passed into the method is within the range of -273 to 3000.
        
        Args:
            temp (int): the value of the temperature in celsius.
            
        Returns:
            bool: true if temperature value is within range; False otherwise.
        """
        if temp > -273 and temp < 3000:
            return True
        else:
            return False
        
    @classmethod
    def temp_fahren(cls,fahren_temp):
        """Create temperature class using fahrenheit
        
        Can be used to create the temperature class using fahrenheit instead of celsius
        
        Args:
            fahren_temp (int): the value of the temperature in fahrenheit
            
        Returns: 
            temperature: the temperature created using fahrenheit temperature value
        """
        temp_fahren = cls.temp_celsius(fahren_temp)
        return cls(temp_fahren)
        
        
    @classmethod
    def standard(cls,celsius = 0):
        """Standard temperature 
        
        Used to create a new instance of temperature with default celsius value of 0
        
        Args:
            celsius (int): the value of the temperature, default = 0
            
        Returns:
            temperature: the temperature created using celsius value
        """
        standard_temp = cls(celsius)
        return standard_temp
        
        