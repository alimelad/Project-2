import random

class MarketEnvironment:
    def __init__(self, environment_name, num_buyers, num_sellers, token_values_range):
        self.environment_name = environment_name
        self.buyers = []
        self.sellers = []
        self.num_buyers = num_buyers
        self.num_sellers = num_sellers
        self.token_values_range = token_values_range
        self.trades = []

    def add_buyer(self, buyer):
        self.buyers.append(buyer)

    def add_seller(self, seller):
        self.sellers.append(seller)

    def simulate_market(self, num_rounds):
        for _ in range(num_rounds):
            for buyer in self.buyers:
                bid = buyer.bid()
                if bid:
                    for seller in self.sellers:
                        ask = seller.ask()
                        if ask and bid >= ask:
                            trade_price = (bid + ask) // 2
                            self.trades.append((trade_price, buyer.name, seller.name))
                            buyer.contract(trade_price, True)
                            seller.contract(trade_price, True)
                            break

    def summarize_results(self):
        total_trades = len(self.trades)
        total_profit = sum([trade[0] for trade in self.trades])
        return {
            "Environment": self.environment_name,
            "Total Trades": total_trades,
            "Total Profit": total_profit,
        }
