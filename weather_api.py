import requests
import re
from lxml import html
from time import time
from datetime import datetime, timedelta

class WeatherService:
    def __init__(self):
        self.api_app_url_summary = 'http://www.meteo-paris.com/ile-de-france/previsions.php'
        self.api_app_url_temperatures = 'http://www.meteo-paris.com/accueil/jour_plus/'
        self.api_app_url_icons = 'http://www.meteo-paris.com/accueil/jour_plus/'
        self.summary = ''
        self.temperatures_today = []
        self.temperatures_tomorrow = []
        self.icons_today = []
        self.icons_tomorrow = []
        self.last_update_summary = 0
        self.last_update_temperatures = 0
        self.last_update_icons = 0

    def get_weather_summary(self, tomorrow):
        if time() - 1800 > self.last_update_summary:
            try:
                r = requests.get(self.api_app_url_summary)
                tree = html.fromstring(r.content)
                if tomorrow:
                    self.summary = tree.xpath('//span[@class="vertical_com_15j"]/p/text()')[1]
                else:
                    self.summary = tree.xpath('//span[@class="vertical_com_15j"]/p/text()')[0]
                self.last_update_summary = time()
            except TimeoutError:
                print('Timeout Error')
                return 'Timeout Error'
            except ConnectionError:
                print('Connection Error')
                return 'Connection Error'
        return self.summary

    def get_weather_temperatures(self, tomorrow):
        if time() - 1800 > self.last_update_temperatures:
            # The POST request can only get next day's weather, so we need today if we need tomorrow's weather
            reference_date = datetime.now() if tomorrow else datetime.now() - timedelta(days=1)
            timestamp = datetime.timestamp(reference_date)
            try:
                r = requests.get(self.api_app_url_temperatures + str(timestamp))
                tree = html.fromstring(r.content)
                morning_temp = int(tree.xpath('//div[@class="ac_temp"]/text()')[0])
                afternoon_temp = int(tree.xpath('//div[@class="ac_temp"]/text()')[2])
                evening_temp = int(tree.xpath('//div[@class="ac_temp"]/text()')[4])
                if tomorrow:
                    self.temperatures_tomorrow = [morning_temp, afternoon_temp, evening_temp]
                else:
                    self.temperatures_today = [morning_temp, afternoon_temp, evening_temp]
            except TimeoutError:
                print('Timeout Error')
                return 'Timeout Error'
            except ConnectionError:
                print('Connection Error')
                return 'Connection Error'
        return self.temperatures_tomorrow if tomorrow else self.temperatures_today

    def get_weather_icons(self, tomorrow):
        if time() - 1800 > self.last_update_icons:
            # The POST request can only get next day's weather, so we need today if we need tomorrow's weather
            reference_date = datetime.now() if tomorrow else datetime.now() - timedelta(days=1)
            timestamp = datetime.timestamp(reference_date)
            try:
                r = requests.get(self.api_app_url_icons + str(timestamp))
                tree = html.fromstring(r.content)
                morning_icon = int(re.search('/([0-9]*).png', tree.xpath('//img[@class="jBox"]/@src')[0]).group(1))
                afternoon_icon = int(re.search('/([0-9]*).png', tree.xpath('//img[@class="jBox"]/@src')[1]).group(1))
                evening_icon = int(re.search('/([0-9]*).png', tree.xpath('//img[@class="jBox"]/@src')[2]).group(1))
                morning_icon = 36 if morning_icon > 36 else morning_icon
                afternoon_icon = 36 if afternoon_icon > 36 else afternoon_icon
                evening_icon = 36 if evening_icon > 36 else evening_icon
                if tomorrow:
                    self.icons_tomorrow = [morning_icon, afternoon_icon, evening_icon]
                else:
                    self.icons_today = [morning_icon, afternoon_icon, evening_icon]
            except TimeoutError:
                print('Timeout Error')
                return 'Timeout Error'
            except ConnectionError:
                print('Connection Error')
                return 'Connection Error'
        return self.icons_tomorrow if tomorrow else self.icons_today

