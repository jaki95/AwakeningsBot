import requests
import os

chat_id = os.environ.get('AWK-CHAT')
bot_api = os.environ.get('AWK-BOT')
bot_url = "https://api.telegram.org/bot"+bot_api+"/"


def send_message(text):
    """
    Takes the chat id of a telegram bot and the text that was  crawled from the
    website and sends it to the bot
    Args: chat_id = string; chat id of the telegram bot,
          text = string; crawled text to be sent
    Returns: None
    """
    parameters = {'chat_id': chat_id, 'text': text}
    message = requests.post(bot_url + 'sendMessage', data=parameters)
