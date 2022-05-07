from json.tool import main
from re import S
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import LineBotApiError

from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('o8eopUX9WeQUMKcG/OuI0H+hxKKYDJ5dxW92GID+64P0Q0NiXZyS0Ugq0FK1RlhgOhdZZmGVf9bfSPNhEBVdzozi8C+xp6P1DBZV9zoEUo25b0SfqC+WAWYDdTTmbz4vlvoWI/Lrz41+GZu0melU7QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f7d962545857c758db70dc848e29c63b')


# @app.route("/callback", methods=['POST'])
# def callback():
#     # get X-Line-Signature header value
#     signature = request.headers['X-Line-Signature']

#     # get request body as text
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)

#     # handle webhook body
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         print("Invalid signature. Please check your channel access token/channel secret.")
#         abort(400)

#     return 'OK'

# #line_bot_api.broadcast(TextSendMessage(text='Hello!'))

# profile = line_bot_api.get_profile('U057857240e6f1a0f143fff44e4f73569') # 通過使用者id，獲取使用者資訊

# print(profile.display_name)
# print(profile.user_id)
# print(profile.picture_url)
# print(profile.status_message)


# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     msg = event.message.text
#     if msg in ['Hi', 'hi']:
#         reply = 'Hi 87'
#     elif msg in ['你是', '你是?', '妳是', '妳是?', '你是誰', '妳是誰', '你是誰?', '妳是誰?']:
#         reply = '我是誰很重要嗎?'
#     elif msg in ['白痴', '白癡', '白吃', '87']:
#         sticker_message = StickerSendMessage(
#         package_id='446',
#         sticker_id='2019'
#         )
#         line_bot_api.reply_message(
#         event.reply_token,
#         sticker_message)

#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=reply))

# # rich_menu_created
# # rich_menu_to_create = RichMenu(
# #     size = RichMenuSize(width=2500, height=843),
# #     selected = False,
# #     name = "Nice richmenu",
# #     chat_bar_text = "Tap here",
# #     areas = [RichMenuArea(
# #         bounds = RichMenuBounds(x=0, y=0, width=2500, height=843),
# #         action = URIAction(label='Go to line.me', uri='https://line.me'))]
# # )
# # rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)



# if __name__ == "__main__":
#     app.run()

# # git add .
# # git commit -m "xx"
# # git push origin main
# # heroku login
# # git push heroku main

# from linebot import LineBotApi
# from linebot.exceptions import LineBotApiError

# rich_menu_list = line_bot_api.get_rich_menu_list()
# print(rich_menu_list)

# # Get rich-menu
# rich_menu = line_bot_api.get_rich_menu('U057857240e6f1a0f143fff44e4f73569')




import requests
import json
# 設定 headers，輸入你的 Access Token，記得前方要加上「Bearer 」( 有一個空白 )
headers = {'Authorization':'Bearer o8eopUX9WeQUMKcG/OuI0H+hxKKYDJ5dxW92GID+64P0Q0NiXZyS0Ugq0FK1RlhgOhdZZmGVf9bfSPNhEBVdzozi8C+xp6P1DBZV9zoEUo25b0SfqC+WAWYDdTTmbz4vlvoWI/Lrz41+GZu0melU7QdB04t89/1O/w1cDnyilFU=','Content-Type':'application/json'}

body = {
    'size': {'width': 2500, 'height': 1686},   # 設定尺寸
    'selected': 'true',                        # 預設是否顯示
    'name': 'Richmenu demo',                   # 選單名稱
    'chatBarText': 'Richmenu demo',            # 選單在 LINE 顯示的標題
    'areas':[                                  # 選單內容
        {
          'bounds': {'x': 341, 'y': 75, 'width': 560, 'height': 340}, # 選單位置與大小
          'action': {'type': 'message', 'text': '電器'}                # 點擊後傳送文字
        },
        {
          'bounds': {'x': 1434, 'y': 229, 'width': 930, 'height': 340},
          'action': {'type': 'message', 'text': '運動用品'}
        },
        {
          'bounds': {'x': 122, 'y': 641, 'width':560, 'height': 340},
          'action': {'type': 'message', 'text': '客服'}
        },
        {
          'bounds': {'x': 1012, 'y': 645, 'width': 560, 'height': 340},
          'action': {'type': 'message', 'text': '餐廳'}
        },
        {
          'bounds': {'x': 1813, 'y': 677, 'width': 560, 'height': 340},
          'action': {'type': 'message', 'text': '鞋子'}
        },
        {
          'bounds': {'x': 423, 'y': 1203, 'width': 560, 'height': 340},
          'action': {'type': 'message', 'text': '美食'}
        },
        {
          'bounds': {'x': 1581, 'y': 1133, 'width': 560, 'height': 340},
          'action': {'type': 'message', 'text': '衣服'}
        }
    ]
  }

# Upload rich menu image
with open('D:/Pan/996.PythonTest/line-bot/pic/1.jpg', 'r') as f:
    line_bot_api.set_rich_menu_image('U057857240e6f1a0f143fff44e4f73569', 'image/jpeg', f)

# print('POST','https://api.line.me/v2/bot/user/all/richmenu/U057857240e6f1a0f143fff44e4f73569')

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                      headers=headers,data=json.dumps(body).encode('utf-8'))
print(req.text)
