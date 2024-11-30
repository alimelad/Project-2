import random

class Seller:
    def __init__(self, name, unit_costs):
        self.name = name
        self.type = 'S'
        self.unit_costs = sorted(unit_costs)
        self.current_unit = 0
        self.prices = []
        self.contracts = []

    def ask(self, standing_ask):
        if self.current_unit < len(self.unit_costs) and self.unit_costs[self.current_unit] < standing_ask:
            return self.name, "ask", random.randint(self.unit_costs[self.current_unit], standing_ask)
        return None

    def contract(self, price, your_contract):
        self.prices.append(price)
        if your_contract:
            self.contracts.append(price)
            self.current_unit += 1
