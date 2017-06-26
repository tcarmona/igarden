import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)

p = GPIO.PWM(7,50)
p.start(7.5)

try:
	while True:
		p.ChangeDutyCycle(7.5)
		print("Position 1")
		time.sleep(2)
		p.ChangeDutyCycle(12.5)
		print("Position 2")
		time.sleep(2)
		p.ChangeDutyCycle(2.5)
		print("Position 3")
		time.sleep(2)

except KeyboardInterrupt:
	GPIO.cleanup()
