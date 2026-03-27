from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class PaymentResult:
    sucess: bool
    transaction_id: str | None
    error_message: str | None

class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, amount: float, currency: str) -> PaymentResult:
        ...