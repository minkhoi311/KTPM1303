from src.product import Product
from src.discount import Discount
from typing import Optional

class LineItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items: list[LineItem] = []

    def add_item(self, product:Product, quantity:int) -> None:
        if product is None or quantity <=0:
            raise ValueError("Product and quantity must be positive")
        self.items.append(LineItem(product, quantity))

    def calculate_total(self, discount: Optional[Discount]) -> float:
        subtotal = sum(
            line.product.price * line.quantity for line in self.items
            )
        if discount is not None:
            subtotal = subtotal * (100 - discount.percentage) /100
        return (subtotal * 100) / 100
    @property
    def item_count(self) -> int:
        return len(self.items)