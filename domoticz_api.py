import requests
from credentials import *

domoticz_api_app_url = 'http://192.168.1.6:8080/json.htm'


def get_temperature(device_index):
    # headers = {'content-type': 'application/json'}
    parameters = {
        "username": domoticz_username,
        "password": domoticz_password,
        "type": "devices",
        "rid": device_index,
    }

    r = requests.post(domoticz_api_app_url, params=parameters)

    return float(r.json()['result'][0]['Data'][:-2])


def get_power(device_index):
    # headers = {'content-type': 'application/json'}
    parameters = {
        "username": domoticz_username,
        "password": domoticz_password,
        "type": "devices",
        "rid": device_index,
    }

    r = requests.post(domoticz_api_app_url, params=parameters)

    return int(r.json()['result'][0]['Data'][:-5])
