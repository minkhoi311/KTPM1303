import pytest
from src.caculator import Caculator

@pytest.fixture
def caculator():
    return Caculator()
    """Mỗi test case nhận instanced Caculator mới (Indenpendence)"""

def test_and_posititive_number_return_sum(caculator):
    #ACT
    result = caculator.add(2,3)
    # ASSERT
    assert result ==5

def test_and_negative_number_return_sum(caculator):
    #ACT
    result = caculator.add(-2, -3)
    # ASSERT
    assert result == -5

def test_subtract_posititive_number_return_sum(caculator):
    #ACT
    result = caculator.subtract(5,3)
    # ASSERT
    assert result == 2

def test_multi_posititive_number_return_sum(caculator):
    #ACT
    result = caculator.multiply(5,3)
    # ASSERT
    assert result == 15

def test_multi_negative_number_return_sum(caculator):
    #ACT
    result = caculator.multiply(5,-3)
    # ASSERT
    assert result == -15

def test_divide_positive_number_return_sum(caculator):
    #ACT
    result = caculator.divide(5,2)
    # ASSERT
    assert result == 2.5

def test_divide_positive_number_return_zero(caculator):
    #ACT
    with pytest.raises(ValueError) as  exc_info:
        caculator.divide(5,0)
    # ASSERT
    assert "Cannot divide by zero" in str(exc_info.value)