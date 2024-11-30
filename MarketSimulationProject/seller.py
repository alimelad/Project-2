import random

class Seller:
    def __init__(self, name, unit_costs, strategy="default"):
        self.name = name
        self.unit_costs = sorted(unit_costs)
        self.current_unit = 0
        self.strategy = strategy
        self.prices = []
        self.contracts = []

    def ask(self):
        if self.strategy == "adaptive" and self.prices:
            avg_price = sum(self.prices) / len(self.prices)
            return min(self.unit_costs[self.current_unit], avg_price)
        elif self.strategy == "random_choice":
            return random.randint(10, 200)
        elif self.current_unit < len(self.unit_costs):
            return self.unit_costs[self.current_unit]
        return None

    def contract(self, price, success):
        if success:
            self.prices.append(price)
            self.current_unit += 1
