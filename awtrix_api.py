import requests


def display_text(text, color):
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


def show_high_low_temp(temperatures):
    api_app_url = 'http://192.168.1.6:7000/api/v3/draw'
    headers = {'content-type': 'application/json'}

    payload = {
        "repeat": 0,
        "draw": [
            {
                "type": "line",
                "start": [4, 7],
                "end": [14, 7],
                "color": [180, 180, 180]
            },
            {
                "type": "line",
                "start": [16, 7],
                "end": [26, 7],
                "color": [100, 100, 100]
            },
            {
                "type": "text",
                "string": temperatures[0],
                "position": [4, 1],
                "color": [10, 10, 255]
            },
            {
                "type": "text",
                "string": temperatures[1],
                "position": [18, 1],
                "color": [250, 0, 0]
            },
            {
                "type": "text",
                "string": "/",
                "position": [13, 1],
                "color": [200, 200, 200]
            },
            {
                "type": "show"
            },
            {
                "type": "wait",
                "ms": 3000
            },
            {
                "type": "clear",
            },
            {
                "type": "line",
                "start": [4, 7],
                "end": [14, 7],
                "color": [100, 100, 100]
            },
            {
                "type": "line",
                "start": [16, 7],
                "end": [26, 7],
                "color": [180, 180, 180]
            },
            {
                "type": "text",
                "string": temperatures[2],
                "position": [4, 1],
                "color": [10, 10, 255]
            },
            {
                "type": "text",
                "string": temperatures[3],
                "position": [18, 1],
                "color": [250, 0, 0]
            },
            {
                "type": "text",
                "string": "/",
                "position": [13, 1],
                "color": [200, 200, 200]
            },
            {
                "type": "show"
            },
            {
                "type": "wait",
                "ms": 3000
            },
            {
                "type": "exit"
            }
        ]

    }

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


def show_external_temp(temperature):
    api_app_url = 'http://192.168.1.6:7000/api/v3/draw'
    headers = {'content-type': 'application/json'}

    payload = {
        "repeat": 10,
        "draw": [
            {
                "position": [0, 0],
                "type": "bmp",
                "size": [5, 8],
                "data": [0, 45116, 45116, 45116, 0,
                         45116, 65534, 65534, 65534, 45116,
                         45116, 65534, 65472, 65534, 45116,
                         45116, 65534, 65534, 65534, 45116,
                         0, 45116, 45116, 45116, 0,
                         1609, 0, 1609, 0, 1609,
                         1609, 1609, 1609, 1609, 1609,
                         0, 0, 1609, 0, 0]
            },
            {
                "type": "text",
                "string": '{0:>5.1f}°'.format(temperature),
                "position": [8, 1],
                "color": [246, 0, 242]
            },
            {
                "type": "show"
            },
            {
                "type": "wait",
                "ms": 1000
            },
            {
                "type": "exit"
            }
        ]

    }

    r = requests.post(api_app_url, json=payload, headers=headers)


def show_power(power):
    api_app_url = 'http://192.168.1.6:7000/api/v3/draw'
    headers = {'content-type': 'application/json'}

    color = [255, 0, 0] if power > 1500 else [255, 255, 0] if power > 750 else [0, 255, 0]

    payload = {
        "repeat": 1,
        "draw": [
            {
                "position": [0, 0],
                "type": "bmp",
                "size": [4, 8],
                "data": [0, 0, 65159, 0,
                         0, 64071, 0, 0,
                         65415, 0, 0, 0,
                         41287, 41287, 41287, 41287,
                         0, 0, 0, 65415,
                         64135, 0, 64071, 0,
                         64135, 65159, 0, 0,
                         64135, 64135, 64135, 0]
            },
            {
                "type": "text",
                "string": '{:>4} W'.format(power),
                "position": [8, 1],
                "color": color
            },
            {
                "type": "show"
            },
            {
                "type": "wait",
                "ms": 0
            },
            {
                "position": [0, 0],
                "type": "bmp",
                "size": [4, 8],
                "data": [0, 0, 41287, 0,
                         0, 65159, 0, 0,
                         65415, 0, 0, 0,
                         65415, 41287, 41287, 41287,
                         0, 0, 0, 41287,
                         64135, 0, 65415, 0,
                         64135, 65415, 0, 0,
                         64135, 64135, 64135, 0]
            },
            {
                "type": "show"
            },
            {
                "type": "wait",
                "ms": 100
            },
            {
                "position": [0, 0],
                "type": "bmp",
                "size": [4, 8],
                "data": [0, 0, 41287, 0,
                         0, 64135, 0, 0,
                         65159, 0, 0, 0,
                         65415, 65415, 65415, 41287,
                         0, 0, 0, 41287,
                         64135, 0, 41287, 0,
                         64135, 41287, 0, 0,
                         64135, 64135, 64135, 0]
            },
            {
                "type": "show"
            },
            {
                "type": "wait",
                "ms": 1000
            },

            {
                "type": "exit"
            }
        ]

    }

    r = requests.post(api_app_url, json=payload, headers=headers)
