import json


def get_paper_balance():
    with open("config/paper_balance.json", "r") as read_file:
        return json.load(read_file)


def write_paper_balance(new_balance):
    with open("config/paper_balance.json", "w") as write_file:
        json.dump(new_balance, write_file, indent=1)


def get_config():
    with open("app/config/config.json", "r") as read_file:
        return json.load(read_file)


def notice(msg):
    if len(str(get_config()["telegram_chat_id"])) and len(get_config()["telegram_token"]) > 1:
        t = Telegram()
        t.send_message(msg)
    else:
        print(msg)