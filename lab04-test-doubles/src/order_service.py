from .payment_gateway import PaymentResult
from src.payment_gateway import PaymentGateway

class OrderServices:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def place_order(self, order_id: str, total_amount: float, currency: str) -> bool:
        result = self.payment_gateway.charge(total_amount, currency)
        return result.sucess