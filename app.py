from awtrix_api import *
from domoticz_api import get_temperature, get_power
from weather_api import *
from time import sleep
import color_constants


# while(1):
#      display_text('Jardin: ' + get_temperature(80), color_constants.ALICEBLUE)
#      display_text(get_power(190), color_constants.GOLD1)
#      display_text('Jardin: ' + get_temperature(80), color_constants.ALICEBLUE)
#      display_text(get_power(190), color_constants.GOLD1)
#      sleep(90)
#      display_text(get_weather_summary(), color_constants.DARKORANGE)
#      display_text(get_power(190), color_constants.GOLD1)
#      display_text('Jardin: ' + get_temperature(80), color_constants.ALICEBLUE)
#      display_text(get_power(190), color_constants.GOLD1)
#      display_text('Jardin: ' + get_temperature(80), color_constants.ALICEBLUE)
#      display_text(get_power(190), color_constants.GOLD1)
#      sleep(90)



# while(1):
#     show_power(get_power(190))
#     sleep(10)
#     show_external_temp(get_temperature(80))
#     sleep(10)
#     sleep(90)

# weather_service = WeatherService()
#
# while(1):
#     display_text(weather_service.get_weather_summary(tomorrow=False), color_constants.GOLD1)
#     sleep(60)
#     display_text(weather_service.get_weather_summary(tomorrow=True), color_constants.INDIANRED)
#     sleep(60)


weather_service = WeatherService()
icons = weather_service.get_weather_icons(tomorrow=False)
temperatures = weather_service.get_weather_temperatures(tomorrow=False)
show_weather_symbols(False, icons[0], icons[1], icons[2])
sleep(3)
show_weather_temperatures(False, temperatures[0], temperatures[1], temperatures[2])
sleep(3)

print(weather_service.get_weather_icons(tomorrow=True))
