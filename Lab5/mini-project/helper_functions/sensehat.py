import time
from sense_hat import SenseHat

# This function returns a SenseHat instance
def get_sensehat():
    sense = SenseHat()
    return sense

# This function takes in a SenseHat instance and the flash_time The display on the SenseHat flashes red (1 second on,
# 1 second off) for the duration of flash_time. At the end of the flash_time the SenseHat display should be off.
def alarm(sense,flash_time):
    red_color = (255, 0, 0)

    for i in range (flash_time):
        sense.clear(red_color)
        time.sleep(1)
        sense.clear()
        time.sleep(1)
