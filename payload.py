from weather_icons import weather_icons


class Payload:
    def __init__(self):
        self.draw = []

    def add_weather_temperatures(self, tomorrow, morning, afternoon, evening):
        upper_color = [100, 100, 100] if tomorrow else [180, 180, 180]
        lower_color = [180, 180, 180] if tomorrow else [100, 100, 100]

        morning_color = [10, 10, 255] if morning < 0 else [250, 0, 0]
        afternoon_color = [10, 10, 255] if afternoon < 0 else [250, 0, 0]
        evening_color = [10, 10, 255] if evening < 0 else [250, 0, 0]

        self.draw.append({"type": "clear"})
        self.draw.append({"type": "line", "start": [0, 0], "end": [0, 3], "color": upper_color})
        self.draw.append({"type": "line", "start": [0, 4], "end": [0, 8], "color": lower_color})
        self.draw.append({"type": "text", "string": '{:>2}'.format(abs(morning)), "position": [3, 1], "color": morning_color})
        self.draw.append({"type": "text", "string": '{:>2}'.format(abs(afternoon)), "position": [13, 1], "color": afternoon_color})
        self.draw.append({"type": "text", "string": '{:>2}'.format(abs(evening)), "position": [23, 1], "color": evening_color})
        self.draw.append({"type": "show"})
        self.draw.append({"type": "wait", "ms": 8000})

    def add_weather_icons(self, tomorrow, morning, afternoon, evening):
        upper_color = [100, 100, 100] if tomorrow else [180, 180, 180]
        lower_color = [180, 180, 180] if tomorrow else [100, 100, 100]

        self.draw.append({"type": "clear"})
        self.draw.append({"type": "line", "start": [0, 0], "end": [0, 3], "color": upper_color})
        self.draw.append({"type": "line", "start": [0, 4], "end": [0, 8], "color": lower_color})
        self.draw.append({"type": "bmp", "position": [3, 0], "size": [8, 8], "data": weather_icons[morning - 1]})
        self.draw.append({"type": "bmp", "position": [13, 0], "size": [8, 8], "data": weather_icons[afternoon - 1]})
        self.draw.append({"type": "bmp", "position": [23, 0], "size": [8, 8], "data": weather_icons[evening - 1]})
        self.draw.append({"type": "show"})
        self.draw.append({"type": "wait", "ms": 8000})

    def add_external_temp(self, temperature):
        self.draw.append({"type": "clear"})
        self.draw.append({"position": [0, 0], "type": "bmp", "size": [5, 8],
                          "data": [0, 45116, 45116, 45116, 0, 45116, 65534, 65534,
                                   65534, 45116, 45116, 65534, 65472, 65534, 45116, 45116,
                                   65534, 65534, 65534, 45116, 0, 45116, 45116, 45116,
                                   0, 1609, 0, 1609, 0, 1609, 1609, 1609,
                                   1609, 1609, 1609, 0, 0, 1609, 0, 0]
                          })
        self.draw.append({"type": "text", "string": '{0:>5.1f}°'.format(temperature), "position": [8, 1], "color": [246, 0, 242]})
        self.draw.append({"type": "show"})
        self.draw.append({"type": "wait", "ms": 4000})


    def add_power(self, power):
        color = [255, 0, 0] if power > 1500 else [255, 255, 0] if power > 750 else [0, 255, 0]

        self.draw.append({"type": "clear"})
        self.draw.append({"position": [0, 0], "type": "bmp", "size": [4, 8],
                          "data": [0, 0, 65159, 0,
                                   0, 64071, 0, 0,
                                   65415, 0, 0, 0,
                                   41287, 41287, 41287, 41287,
                                   0, 0, 0, 65415,
                                   64135, 0, 64071, 0,
                                   64135, 65159, 0, 0,
                                   64135, 64135, 64135, 0]
                          })
        self.draw.append({"type": "text", "string": '{:>4} W'.format(power), "position": [8, 1], "color": color})
        self.draw.append({"type": "show"})
        self.draw.append({"type": "wait", "ms": 100})
        self.draw.append({"position": [0, 0], "type": "bmp", "size": [4, 8],
                          "data": [0, 0, 41287, 0,
                                   0, 65159, 0, 0,
                                   65415, 0, 0, 0,
                                   65415, 41287, 41287, 41287,
                                   0, 0, 0, 41287,
                                   64135, 0, 65415, 0,
                                   64135, 65415, 0, 0,
                                   64135, 64135, 64135, 0]
                          })
        self.draw.append({"type": "show"})
        self.draw.append({"type": "wait", "ms": 100})
        self.draw.append({"position": [0, 0], "type": "bmp", "size": [4, 8],
                          "data": [0, 0, 41287, 0,
                                   0, 64135, 0, 0,
                                   65159, 0, 0, 0,
                                   65415, 65415, 65415, 41287,
                                   0, 0, 0, 41287,
                                   64135, 0, 41287, 0,
                                   64135, 41287, 0, 0,
                                   64135, 64135, 64135, 0]
                          })
        self.draw.append({"type": "show"})
        self.draw.append({"type": "wait", "ms": 4000})

    def get_payload(self):
        self.draw.append({"type": "exit"})
        payload = {}
        payload["repeat"] = 0
        payload["draw"] = self.draw

        return payload
