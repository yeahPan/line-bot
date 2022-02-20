from re import S
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('o8eopUX9WeQUMKcG/OuI0H+hxKKYDJ5dxW92GID+64P0Q0NiXZyS0Ugq0FK1RlhgOhdZZmGVf9bfSPNhEBVdzozi8C+xp6P1DBZV9zoEUo25b0SfqC+WAWYDdTTmbz4vlvoWI/Lrz41+GZu0melU7QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f7d962545857c758db70dc848e29c63b')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if msg in ['Hi', 'hi']:
        reply = 'Hi 87'
    elif msg in ['你是', '你是?', '妳是', '妳是?']:
        reply = '我是誰很重要嗎?'
    elif msg in ['白痴', '白癡', '白吃', '87']:
        reply = '你才白痴!! 你全家都白痴!'

        sticker_message = StickerSendMessage(
        package_id='1',
        sticker_id='1'
        )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))


if __name__ == "__main__":
    app.run()