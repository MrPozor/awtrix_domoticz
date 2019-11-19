import requests
from lxml import html
from time import time
from datetime import datetime, timedelta

class WeatherService:
    def __init__(self):
        self.api_app_url_summary = 'http://www.meteo-paris.com/ile-de-france/previsions.php'
        self.api_app_url_temperatures = 'http://www.meteo-paris.com/ile-de-france/previsions.php'
        self.api_app_url_icons = 'http://www.meteo-paris.com/accueil/jour_plus/'
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

    def get_weather_icons(self, tomorrow):
        # The POST request can only get next day's weather, so we need today if we need tomorrow's weather
        reference_date = datetime.now() if tomorrow else datetime.now() - timedelta(days=1)
        timestamp = datetime.timestamp(reference_date)
        try:
            r = requests.get(self.api_app_url_icons + str(timestamp))
            tree = html.fromstring(r.content)
            print(tree.xpath('//img[@class="jBox"]/@src')[0])
            print(tree.xpath('//img[@class="jBox"]/@src')[1])
            print(tree.xpath('//img[@class="jBox"]/@src')[2])
            print(tree.xpath('//img[@class="jBox"]/@src')[3])
        except TimeoutError:
            print('Timeout Error')
            return 'Timeout Error'
        except ConnectionError:
            print('Connection Error')
            return 'Connection Error'
        return 0
