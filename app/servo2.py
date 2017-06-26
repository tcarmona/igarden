import wiringpi
import time


wiringpi.wiringPiSetup()

wiringpi.pinMode(12, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

#divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.01

while TRUE:
	for pulse in range(50, 250, 1):
		wiringpi.pmwWrite(18, pulse)
		time.sleep(delay_period)
	for pulse in range(250, 50, -1):
		wiringpi.pmwWrite(18, pulse)
		time.sleep(delay_period)

