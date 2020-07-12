from app.modules.exchange import Exchange
from app.modules.trader import Trader


class PipeSimpleBot:
    def __init__(self):
        self.__set_coins()
        exchange = self.__get_exchange(self.coin1, self.coin2, self.coin_pair)
        trader = self.__get_trader(self.coin1, self.coin2, self.coin_pair, exchange)
        self.__execute(trader, exchange)

    def __set_coins(self):
        self.coin1 = "ETH"
        self.coin2 = "BTC"
        self.coin_pair = f"{self.coin1}/{self.coin2}"

    @staticmethod
    def __get_exchange(coin1, coin2, coin_pair):
        return Exchange(coin_pair=coin_pair, coin1=coin1, coin2=coin2)

    @staticmethod
    def __get_trader(coin1, coin2, coin_pair, exchange):
        return Trader(coin_pair=coin_pair, coin1=coin1, coin2=coin2, exchange=exchange)

    @staticmethod
    def __execute(trader, exchange):
        while True:
            if trader.breakout_detect() == "down":
                order = exchange.order(exchange.balance()[1] / exchange.price(), "buy")
                if order is True:
                    if trader.trail_stop() == "sell":
                        amount = exchange.balance()[0]
                        exchange.order(amount, "sell")
