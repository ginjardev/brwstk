""" This is a calculator module"""

class Calculator:
    """The Calculator class """

    def validate_input(self, x, y):

        if isinstance(x, int) and isinstance(y, int):
            return [x, y]
        raise TypeError('enter an integer value not string')

    def add(self, x, y):
        x, y = self.validate_input(x, y)
        return x + y
    
    def minus(self, x, y):
        x, y = self.validate_input(x, y)
        return x - y
    
    def multiply(self, x, y):
        x, y = self.validate_input(x, y)
        return x * y
    
    def divide(self, x, y):
        x, y = self.validate_input(x, y)
        if y == 0:
            raise ZeroDivisionError('Enter a non-zero integer')
        return x/y
