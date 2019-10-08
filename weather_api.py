import requests
from lxml import html
from time import time

class WeatherService:
    def __init__(self):
        self.api_app_url_summary = 'http://www.meteo-paris.com/ile-de-france/previsions.php'
        self.api_app_url_temperatures = 'http://www.meteo-paris.com/ile-de-france/previsions.php'
        self.summary = ''
        self.temperatures = []
        self.last_update_summary = 0
        self.last_update_temperatures = 0

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

    def get_weather_temperatures(self):
        if time() - 1800 > self.last_update_temperatures:
            try:
                r = requests.get(self.api_app_url_temperatures)
                tree = html.fromstring(r.content)
                low_temperatures = tree.xpath('//div[@class="tempMat"]/text()')
                high_temperatures = tree.xpath('//div[@class="tempApm"]/text()')
                self.temperatures = [low_temperatures[0].strip(), high_temperatures[0].strip(), \
                       low_temperatures[1].strip(), high_temperatures[1].strip()]
                self.last_update_temperatures = time()
            except TimeoutError:
                print('Timeout Error')
            except ConnectionError:
                print('Connection Error')
        return self.temperatures

