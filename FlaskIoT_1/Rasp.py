import RPi.GPIO as GPIO

pin = 4

def conf():
    GPIO.setwarning(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    
def LEDon():
    GPIO.output(pin, GPIO.HIGH)

def LEDoff():
    GPIO.output(pin, GPIO.LOW)    