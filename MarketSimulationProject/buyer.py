import random

class ReservationValues:
    def __init__(self, owners_name, reservation_values):
        self.owners_name = owners_name
        self.reservation_values = sorted(reservation_values, reverse=True)
        self.current_unit = 0

    @property
    def current(self):
        try:
            return self.reservation_values[self.current_unit]
        except IndexError:
            return None


class Buyer:
    def __init__(self, name, reservation_values):
        self.name = name
        self.type = 'B'
        self.values = ReservationValues(name, reservation_values)
        self.prices = []
        self.contracts = []

    def bid(self, standing_bid):
        if self.values.current and standing_bid < self.values.current:
            return self.name, "bid", random.randint(standing_bid, self.values.current)
        return None

    def contract(self, price, your_contract):
        self.prices.append(price)
        if your_contract:
            self.contracts.append(price)
            self.values.current_unit += 1
