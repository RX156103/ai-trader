import ccxt
import os


class Exchange:
    def __init__(self, coin_pair, coin1, coin2):
        self.key = os.getenv("BINANCE_API_KEY")
        self.secret = os.getenv("BINANCE_API_SECRET")
        self.exchange = ccxt.binance({"apiKey": self.key, "secret": self.secret, "enableRateLimit": False})
        self.coin_pair = coin_pair
        self.coin = coin1
        self.coin2 = coin2
        self.paper_enabled = "yes"


    def price(self):
        def get_price(self):
            return self.exchange.fetch_ticker(self.coin_pair)["last"]

        while True:
            price = get_price(self)
            if price is not None:
                return(price)


    def balance(self):
        if self.paper_enabled == "yes":
            return get_paper_balance()["paper_balance"]
        else:
            return [self.exchange.fetch_balance()[self.coin]["free"], self.exchange.fetch_balance()[self.coin2]["free"]]


    def order(self, amount, order_side):
        price = None
        # params = {}
        params = {'test': True}
        paper_price = self.price()
        if self.paper_enabled == "yes":
            if order_side == "sell":
                new_balance_coin1 = get_paper_balance()["paper_balance"][0] - amount
                new_balance_coin2 = get_paper_balance()["paper_balance"][1] + (paper_price * amount)
                write_paper_balance({"paper_balance": [new_balance_coin1, new_balance_coin2]})
                return True
            elif order_side == "buy":
                new_balance_coin1 = get_paper_balance()["paper_balance"][0] + amount
                new_balance_coin2 = get_paper_balance()["paper_balance"][1] - (paper_price * amount)
                write_paper_balance({"paper_balance": [new_balance_coin1, new_balance_coin2]})
                return True
        else:
            order = self.exchange.create_order(self.coin_pair, 'market', order_side.lower(), amount, price, params)
            return order