import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, StickerSendMessage
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
    return "OK"

def send_image_url(reply_token, img_url):
    try:
        line_bot_api = LineBotApi(channel_access_token)
        img_url += reply_token
        # for demo, hard coded image url, line api only support image over https
        line_bot_api.reply_message(reply_token, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
    except LineBotApiError as e:
        print(e)
    return "OK"

def send_image_url2(img_url):
    try:
        line_bot_api = LineBotApi(channel_access_token)
        img_url += reply_token
        # for demo, hard coded image url, line api only support image over https
        line_bot_api.reply_message(reply_token, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
    except LineBotApiError as e:
        print(e)
    return "OK"


def send_button_message(id, text, buttons):
    pass


def send_sticker(reply_token, all_stikcer):
    try:
        line_bot_api = LineBotApi(channel_access_token)
        if(len(all_stikcer) == 2):
        # for demo, hard coded image url, line api only support image over https
            line_bot_api.reply_message(reply_token,StickerSendMessage(package_id=all_stikcer[0], sticker_id=all_stikcer[1]))
    except LineBotApiError as e:
        line_bot_api.reply_message(reply_token, TextSendMessage(text="no such sticker"))
        print(e)
  