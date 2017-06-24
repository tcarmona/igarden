import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.IN)

for i in range(0,5):
    print GPIO.input(7)
