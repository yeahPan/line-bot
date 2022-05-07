import requests
import json
# 設定 headers，輸入你的 Access Token，記得前方要加上「Bearer 」( 有一個空白 )
headers = {'Authorization':'Bearer o8eopUX9WeQUMKcG/OuI0H+hxKKYDJ5dxW92GID+64P0Q0NiXZyS0Ugq0FK1RlhgOhdZZmGVf9bfSPNhEBVdzozi8C+xp6P1DBZV9zoEUo25b0SfqC+WAWYDdTTmbz4vlvoWI/Lrz41+GZu0melU7QdB04t89/1O/w1cDnyilFU=','Content-Type':'application/json'}

body = {
    'size': {'width': 2500, 'height': 1686},   # 設定尺寸
    'selected': 'true',                        # 預設是否顯示
    'name': 'Richmenu demo',                   # 選單名稱
    'chatBarText': 'Tap to open',            # 選單在 LINE 顯示的標題
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
# 向指定網址發送 request
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                      headers=headers,data=json.dumps(body).encode('utf-8'))
# 印出得到的結果
print(req.text)


from linebot import LineBotApi, WebhookHandler

line_bot_api = LineBotApi('o8eopUX9WeQUMKcG/OuI0H+hxKKYDJ5dxW92GID+64P0Q0NiXZyS0Ugq0FK1RlhgOhdZZmGVf9bfSPNhEBVdzozi8C+xp6P1DBZV9zoEUo25b0SfqC+WAWYDdTTmbz4vlvoWI/Lrz41+GZu0melU7QdB04t89/1O/w1cDnyilFU=')

with open('D:/Pan/996.PythonTest/line-bot/pic/line-rich-menu-demo.jpg', 'rb') as f:
    line_bot_api.set_rich_menu_image('richmenu-7eaf3a31197ed4edbde60d8cd1b4a671', 'image/jpeg', f)

#Set default rich menu
import requests

headers = {'Authorization':'Bearer o8eopUX9WeQUMKcG/OuI0H+hxKKYDJ5dxW92GID+64P0Q0NiXZyS0Ugq0FK1RlhgOhdZZmGVf9bfSPNhEBVdzozi8C+xp6P1DBZV9zoEUo25b0SfqC+WAWYDdTTmbz4vlvoWI/Lrz41+GZu0melU7QdB04t89/1O/w1cDnyilFU='}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-7eaf3a31197ed4edbde60d8cd1b4a671', headers=headers)

print(req.text)