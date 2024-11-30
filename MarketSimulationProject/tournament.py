from buyer import Buyer
from seller import Seller
from market_environment import MarketEnvironment

class Tournament:
    def __init__(self, environment_configs, num_rounds=50):
        self.environments = [
            MarketEnvironment(name, config["num_buyers"], config["num_sellers"], config["token_range"])
            for name, config in environment_configs.items()
        ]
        self.num_rounds = num_rounds

    def run(self):
        results = []
        for env in self.environments:
            for i in range(env.num_buyers):
                env.add_buyer(Buyer(f"buyer_{i+1}", [10, 50, 100], strategy="adaptive"))
            for i in range(env.num_sellers):
                env.add_seller(Seller(f"seller_{i+1}", [10, 20, 30], strategy="random_choice"))

            env.simulate_market(self.num_rounds)
            results.append(env.summarize_results())

        return results
