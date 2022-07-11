import requests
import os

chat_id = os.environ.get('AWK-CHAT')
bot_api = os.environ.get('AWK-BOT')
bot_url = "https://api.telegram.org/bot"+bot_api+"/"


def send_message(text):
    """
    Sends text to Telegram bot
    Args: text = string; crawled text to be sent
    Returns: None
    """
    parameters = {'chat_id': chat_id, 'text': text}
    message = requests.post(bot_url + 'sendMessage', data=parameters)
