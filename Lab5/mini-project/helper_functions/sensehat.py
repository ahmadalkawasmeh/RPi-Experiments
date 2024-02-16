import time
from sense_hat import SenseHat

# This function returns a SenseHat instance
def get_sensehat():
    sense = SenseHat()
    return sense

# This function takes in a SenseHat instance and the flash_time The display on the SenseHat flashes red (1 second on,
# 1 second off) for the duration of flash_time. At the end of the flash_time the SenseHat display should be off.
def alarm(sense,flash_time):
def alarm(sense,flash_time):
    r = (255, 0, 0)
    temp = round(sense.get_temperature(), 1)
    sense.show_message("Temperature: " + str(temp), text_colour=r, scroll_speed=0.05)
    time.sleep(flash_time)
    sense.clear()
