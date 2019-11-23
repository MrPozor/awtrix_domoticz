from awtrix_api import *
from domoticz_api import get_temperature, get_power
from weather_api import *
from payload import Payload
from time import sleep
import color_constants



while 1:

    # 1st scene: Weather icons with temperatures

    weather_service = WeatherService()

    payload = Payload()

    icons = weather_service.get_weather_icons(tomorrow=False)
    temperatures = weather_service.get_weather_temperatures(tomorrow=False)
    payload.add_weather_icons(False, icons[0], icons[1], icons[2])
    payload.add_weather_temperatures(False, temperatures[0], temperatures[1], temperatures[2])

    icons = weather_service.get_weather_icons(tomorrow=True)
    temperatures = weather_service.get_weather_temperatures(tomorrow=True)
    payload.add_weather_icons(True, icons[0], icons[1], icons[2])
    payload.add_weather_temperatures(True, temperatures[0], temperatures[1], temperatures[2])

    send_payload_to_awtrix(payload.get_payload())

    sleep(60)

    # 2nd scene: External temp and power

    payload = Payload()

    external_temp = get_temperature(80)
    power = get_power(190)
    payload.add_external_temp(external_temp)
    payload.add_power(power)

    send_payload_to_awtrix(payload.get_payload())

    sleep (60)

    # 3rd scene: Weather summaries

    send_text_to_awtrix(weather_service.get_weather_summary(tomorrow=False), color_constants.GOLD1)
    sleep(60)
    send_text_to_awtrix(weather_service.get_weather_summary(tomorrow=True), color_constants.INDIANRED)
    sleep(60)


