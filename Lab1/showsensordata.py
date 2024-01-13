from sense_hat import SenseHat

# get the pressure, humidity and temperature readings, round to 1 digit, then display on the LEDs

sense = SenseHat()
sense.clear()

temp = round(sense.get_temperature(), 1)
hum = round(sense.get_humidity(), 1)
press = round(sense.get_pressure(), 1)

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)

while True:
    sense.show_message("Temperature: " + str(temp), text_colour=r, scroll_speed=0.05)
    sense.show_message("Humidity:" + str(hum), text_colour=g, scroll_speed=0.05)
    sense.show_message("Pressure:" + str(press), text_colour=g, scroll_speed=0.05)
