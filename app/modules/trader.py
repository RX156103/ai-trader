import time


class Trader:
    def __init__(self, coin_pair, coin1, coin2, exchange):
        self.trailing_step_percent = 0.2
        self.change_percent = 20
        self.coin_pair = coin_pair
        self.exchange = exchange

    def trail_stop(self):
        start_price = self.exchange.price()
        last_change_percent = 0.0
        current_change_percent = 0.0

        while True:
            if current_change_percent + self.trailing_step_percent >= last_change_percent:
                last_change_percent = current_change_percent
                price = self.exchange.price()
                current_change_percent = ((price - start_price) / start_price) * 100
                time.sleep(5)
                continue
            else:
                return "sell"

    def breakout_detect(self):
        start_price = self.exchange.price()

        while True:
            current_price = self.exchange.price()
            change_percent = ((current_price - start_price) / start_price) * 100
            if change_percent > self.change_percent:
                return "up"
            elif change_percent < - self.change_percent:
                return "down"
            else:
                print(change_percent, "not detected")
                time.sleep(5)
                continue