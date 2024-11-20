import pytest
from calc import Calculator

@pytest.fixture(scope='module')
def calculator_object():
    calculator = Calculator()
    yield calculator
