curl -v -X POST https://api.line.me/v2/bot/richmenu \
-H 'Authorization: Bearer o8eopUX9WeQUMKcG/OuI0H+hxKKYDJ5dxW92GID+64P0Q0NiXZyS0Ugq0FK1RlhgOhdZZmGVf9bfSPNhEBVdzozi8C+xp6P1DBZV9zoEUo25b0SfqC+WAWYDdTTmbz4vlvoWI/Lrz41+GZu0melU7QdB04t89/1O/w1cDnyilFU=' \
-H 'Content-Type: application/json' \
-d \

{
  "size": {
    "width": 2500,
    "height": 1686
  },
  "selected": false,
  "name": "Nice richmenu",
  "chatBarText": "Tap to open",
  "areas": [
    {
      "bounds": {
        "x": 0,
        "y": 0,
        "width": 2500,
        "height": 1686
      },
      "action": {
        "type": "postback",
        "data": "action=buy&itemid=123"
      }
    }
  ]
}

{
  "richMenuId": "richmenu-88c05ef6921ae53f8b58a25f3a65faf7"
}