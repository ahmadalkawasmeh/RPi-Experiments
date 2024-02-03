from gpiozero import LED


class TrafficLights:
    def __init__(self, redPin, amberPin, greenPin):
        self.redPin = redPin
        self.amberPin = amberPin
        self.greenPin = greenPin
        self.greenLed = LED(greenPin)
        self.redLed = LED(redPin)
        self.amberLed = LED(amberPin)

    def red(self):
        self.redLed.on()
        self.greenLed.off()
        self.amberLed.off()

    def amber(self):
        self.amberLed.on()
        self.redLed.off()
        self.greenLed.off()

    def green(self):
        self.greenLed.on()
        self.redLed.off()
        self.amberLed.off()
