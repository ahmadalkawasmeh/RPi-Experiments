from traffic_lights import TrafficLights
from time import sleep
from gpiozero import Button

button = Button(4)
t_f = TrafficLights(13, 19, 26)

while True:
    t_f.red()
    sleep(5)
    t_f.green()
    button.wait_for_press(5)
    t_f.amber()
    sleep(2)
