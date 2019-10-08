import requests
from lxml import html
from time import time

class WeatherService:
    def __init__(self):
        self.api_app_url_summary = 'http://www.meteo-paris.com/'
        self.api_app_url_forecast = 'http://www.meteo-paris.com/ile-de-france/previsions.php'
        self.summary = ''
        self.forecast = []
        self.last_update = 0

    def get_weather_summary(self):
        if time() - 1800 > self.last_update:
            try:
                print('Refreshing....')
                r = requests.get(self.api_app_url_summary)
                tree = html.fromstring(r.content)
                self.summary = tree.xpath('//span[@class="vertical_com txt_left"]/p/text()')[0]
                self.last_update = time()
            except TimeoutError:
                print('Timeout Error')
                return ''
        else:
            print("Summary still fresh.")
        return self.summary

    def get_weather_temperatures(self):
        r = requests.get(self.api_app_url_forecast)
        tree = html.fromstring(r.content)
        low_temperatures = tree.xpath('//div[@class="tempMat"]/text()')
        high_temperatures = tree.xpath('//div[@class="tempApm"]/text()')

        return [low_temperatures[0].strip(), high_temperatures[0].strip(), \
               low_temperatures[1].strip(), high_temperatures[1].strip()]

