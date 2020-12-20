import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError



channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_fsm_graph(reply_token):
    try:
        line_bot_api = LineBotApi(channel_access_token)
        FSM_GRAPH_URL = os.getenv("FSM_GRAPH_URL", None)
        # for demo, hard coded image url, line api only support image over https
        line_bot_api.reply_message(reply_token, ImageSendMessage(original_content_url=FSM_GRAPH_URL, preview_image_url=FSM_GRAPH_URL))
    except LineBotApiError as e:
        print(e)
    return "cool"

def send_image_url(id, img_url):
    pass


def send_button_message(id, text, buttons):
    pass

