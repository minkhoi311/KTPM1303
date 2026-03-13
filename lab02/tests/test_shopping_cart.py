import pytest
from src.product import Product
from src.shopping_cart import ShoppingCart
from src.discount import Discount

@pytest.fixture
def cart():
    return ShoppingCart()

def test_calculate_total_one_product_no_discount_return_subtotal(cart):
    #Arrange
    laptop = Product("Laptop", 1000.0)
    cart.add_item(laptop, 2)

    #act
    total = cart.calculate_total(None)
    #assert
    assert total == 2000.0


def test_calculate_total_with_discount_return_aplies_discount(cart):
    #Arrange
    laptop = Product("Laptop", 1000.0)
    cart.add_item(laptop, 2)
    discount = Discount(10)
    #act
    total = cart.calculate_total(discount)
    #assert
    assert total == 1800.0

def test_calculate_total_empty_cart_return_zero(cart):
    #Arrange
    #act
    total = cart.calculate_total(None)
    #assert
    assert total == 0.0

def test_add_item_null_product_throw_exception(cart):
    #Arrange
    null_product = None
    quantity = 1
    #ACT
    with pytest.raises(ValueError) as  exc_info:
        cart.add_item(null_product, quantity)
    # ASSERT
    assert "Product and quantity must be positive" in str(exc_info.value)
