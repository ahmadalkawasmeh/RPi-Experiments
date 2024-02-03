from traffic_lights import TrafficLights
from time import sleep

def test_traffic_lights():
    t_f = TrafficLights(13, 19, 26)
    sleep(2)
    t_f.red()
    sleep(2)
    if t_f.redLed.value == 1:
        if t_f.greenLed.value != 0:
            raise AssertionError("Green is still on!")
        if t_f.amberLed.value != 0:
            raise AssertionError("Amber is still on!")
    sleep(2)
    t_f.green()
    sleep(2)
    if t_f.greenLed.value == 1:
        if t_f.redLed.value != 0:
            raise AssertionError("Red is still on!")
        if t_f.amberLed.value != 0:
            raise AssertionError("Amber is still on!")
    sleep(2)
    t_f.amber()
    sleep(2)
    if t_f.amberLed.value == 1:
        if t_f.redLed.value != 0:
            raise AssertionError("Red is still on!")
        if t_f.greenLed.value != 0:
            raise AssertionError("Green is still on!")


# Run the test
test_traffic_lights()
