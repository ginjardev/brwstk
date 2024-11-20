from calc import Calculator

def test_add(calculator_object):
    assert calculator_object.add(4, 3) == 7, 'Expected result should be 7'

def test_minus(calculator_object):
    assert calculator_object.minus(10, 5) == 5, 'Expected result should be 5'

def test_multiply(calculator_object):
    assert calculator_object.multiply(4, 6) == 24, 'Expected result should be 24'

def test_divide(calculator_object):
    assert calculator_object.divide(12, 2) == 6, 'Expected result should be 6'
