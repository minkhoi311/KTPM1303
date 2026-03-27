import pytest
from unittest.mock import Mock

from src.order_service import OrderServices
from src.payment_gateway import PaymentResult
from src.payment_gateway import PaymentGateway

def test_place_order_when_charge_succeeds_return_true():
    gateway = Mock()
    gateway.charge.return_value = PaymentResult(True, "TXT-001", None)
    service = OrderServices(gateway)

    result = service.place_order("ORD-001", 100.0, "USD")
    assert result is True

def test_place_order_when_charge_succeeds_return_false():
    gateway = Mock()
    gateway.charge.return_value = PaymentResult(False, None, "Insufficient funds")
    service = OrderServices(gateway)

    result = service.place_order("ORD-002", 50.0, "USD")
    assert result is False

def test_place_order_call_gateway_once_with_correct_amount():
    gateway = Mock()
    gateway.charge.return_value = PaymentResult(True, "TXT-002", None)
    service = OrderServices(gateway)
    service.place_order("ORD-003", 200.0, "VND")
    gateway.charge.assert_called_once_with(200.0, "VND")

def test_place_order_does_not_call_gateway():
    gateway = Mock()
    gateway.charge.return_value = PaymentResult(True, "X", None)
    service = OrderServices(gateway)

    service.place_order("ORD-004", 10.0, "USD")
    assert gateway.charge.call_count == 1
    gateway.charge.assert_called_with(10.0, "USD")

    