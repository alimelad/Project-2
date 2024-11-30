import random

class Buyer:
    def __init__(self, name, reservation_values, strategy="default"):
        self.name = name
        self.reservation_values = sorted(reservation_values, reverse=True)
        self.current_unit = 0
        self.strategy = strategy
        self.prices = []
        self.contracts = []

    def bid(self):
        if self.strategy == "adaptive" and self.prices:
            avg_price = sum(self.prices) / len(self.prices)
            return max(self.reservation_values[self.current_unit], avg_price)
        elif self.strategy == "random_choice":
            return random.randint(10, 200)
        elif self.current_unit < len(self.reservation_values):
            return self.reservation_values[self.current_unit]
        return None

    def contract(self, price, success):
        if success:
            self.prices.append(price)
            self.current_unit += 1
