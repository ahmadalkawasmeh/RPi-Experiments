from sense_hat import SenseHat

# Lab 1
# This is a script to continuously scroll my name on the sense hat, text colour set to red and background colour set to
# white, scroll speed is set to 0.3 and the default speed being 0.1

sense = SenseHat()

while True:
    sense.show_message("Ahmad Alkawasmeh", text_colour=(255, 0, 0), back_colour=(255, 255, 255), scroll_speed=0.3)
