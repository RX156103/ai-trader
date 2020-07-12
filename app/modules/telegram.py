import os
import requests


class Telegram:
    def __init__(self):
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self.token = os.getenv("TELEGRAM_TOKEN")

    def send_message(self, msg):
        try:
            requests.get(f"https://api.telegram.org/bot{self.token}/sendMessage?text={msg}&chat_id={self.chat_id}")
        except Exception as ex:
            raise ex