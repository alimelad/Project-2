import random
from buyer import Buyer
from seller import Seller

class Tournament:
    def __init__(self, strategy1, strategy2, num_rounds=100):
        self.strategy1 = strategy1
        self.strategy2 = strategy2
        self.num_rounds = num_rounds
        self.buyers = []
        self.sellers = []

    def setup_market(self):
        for i in range(2):
            self.buyers.append(Buyer(f"buyer_{i+1}", [10, 50, 100]))
            self.buyers[-1].strategy = self.strategy1

            self.buyers.append(Buyer(f"buyer_{i+3}", [10, 50, 100]))
            self.buyers[-1].strategy = self.strategy2

            self.sellers.append(Seller(f"seller_{i+1}", [10, 20, 30]))
            self.sellers[-1].strategy = self.strategy1

            self.sellers.append(Seller(f"seller_{i+3}", [10, 20, 30]))
            self.sellers[-1].strategy = self.strategy2

    def simulate_rounds(self):
        for _ in range(self.num_rounds):
            # Randomly select a trader to make a bid or ask
            trader = random.choice(self.buyers + self.sellers)
            if trader.type == "B":
                trader.bid(0)
            elif trader.type == "S":
                trader.ask(200)

    def evaluate_market(self):
        # Placeholder for calculating market results
        return {"Efficiency (%)": 90.0}

    def run(self):
        self.setup_market()
        self.simulate_rounds()
        return self.evaluate_market()


if __name__ == "__main__":
    # Running the tournament
    tournament = Tournament("adaptive", "random_choice", num_rounds=50)
    results = tournament.run()
    print("Tournament Results:", results)
