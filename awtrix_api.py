import requests
from weather_icons import weather_icons


def send_text_to_awtrix(text, color):
    api_app_url = 'http://192.168.1.6:7000/api/v3/app'
    headers = {'content-type': 'application/json'}
    payload = {
        "name": "domoticz",
        "force": False,
        "text": text,
        "color": [color.red, color.green, color.blue],
        "count": 1
    }

    r = requests.post(api_app_url, json=payload, headers=headers)


def send_payload_to_awtrix(payload):
    api_app_url = 'http://192.168.1.6:7000/api/v3/draw'
    headers = {'content-type': 'application/json'}
    r = requests.post(api_app_url, json=payload, headers=headers)


def reminder_trash():
    api_app_url = 'http://192.168.1.6:7000/api/v3/draw'
    headers = {'content-type': 'application/json'}
    payload = {
        "repeat": 1,
        "draw": [
            {
                "type": "fill",
                "color": [100, 100, 100]
            },
            {
                "type": "text",
                "string": "Trash!",
                "position": [5, 1],
                "color": [255, 0, 0]
            },
            {
                "type": "show"
            },
            {
                "type": "wait",
                "ms": 0
            },
            {
                "type": "exit"
            }
        ]

    }

    r = requests.post(api_app_url, json=payload, headers=headers)

