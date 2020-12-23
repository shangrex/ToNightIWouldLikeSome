import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from config import help_message
from fsm import TocMachine
from utils import send_text_message, send_image_url


#test
from config import set_machine
from utils import send_fsm_graph
import json
load_dotenv()

int_machine = set_machine()
machine = TocMachine(states= int_machine.state(),
            transitions=int_machine.transition(),
            initial=int_machine.initial(),
            auto_transitions=int_machine.auto_transitions(),
            show_conditions=int_machine.show_conditions(),
            )

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
domain_url = os.getenv("DOMAIN_URL", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

@app.route('/', methods=["POST"])
def root():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)


    for event in events:
            if not isinstance(event, MessageEvent):
                continue
            if not isinstance(event.message, TextMessage):
                continue
            if not isinstance(event.message.text, str):
                continue
            if event.message.text == "help":
                send_text_message(event.reply_token, help_message())
            elif event.message.text == "fsm":
                img_url = domain_url +"show-fsm/"
                app.logger.info(img_url+event.reply_token)
                send_image_url(event.reply_token, img_url)
            else:
                print(f"\nFSM STATE: {machine.state}")
                print(f"REQUEST BODY: \n{body}")
                response = machine.advance(event)
                if response == False:
                    send_text_message(event.reply_token, "Not Entering any State")
    return "OK"

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )
    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


@app.route("/show-fsm/<user_id>", methods=["GET", "POST"])
def show_fsm(user_id):
    path = os.getcwd()
    app.logger.info(domain_url+"show-fsm/"+user_id)
    # machine.get_graph().draw(path+"/fsm.png", prog="dot", format="png")
    # print(webhook["events"][0]["replyToken"])
    # send_fsm_graph(webhook["events"][0]["replyToken"])
    
    return send_file(path+"/fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.getenv("PORT", None)
    app.run(host="0.0.0.0", port=port, debug=True)
