class Discount:
    def __init__(self, percentage: int):
        if not 0 <= percentage <= 100:
            raise ValueError("Discount must be 0-100")
        self.percentage = percentage