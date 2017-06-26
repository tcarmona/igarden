#!/usr/bin/python
 
import RPi.GPIO as GPIO
import spidev
import time
import thingspeak
import urllib

# Define Variables
delay = 20 #Thingspeak free has a delay of 15 seconds for data update
light = 0  #Analog pin of the data cable of the light sensor
soil = 1   #Analog pin of the data cable of the soil moisture sensor
write_key = "EFGX918WTOL8UZKT"
read_key = "6UKWF6OLI9M3OUIQ"
channel_id = "293365"

# Set the GPIO to use the Raspberry Port Numbers
GPIO.setmode(GPIO.BOARD)

# Configure the water pump relay 
GPIO.setup(11, GPIO.OUT) 
GPIO.output(11, GPIO.HIGH)


# Define the servo interface
GPIO.setup(7,GPIO.OUT)
servo = GPIO.PWM(7,50)
servo.start(2.5)
time.sleep(3)
servo.stop()
current_position = 0

# Create SPI, used for the analog sensors
spi = spidev.SpiDev()
spi.open(0, 0)
 
def readadc(adcnum):
    # read SPI data from the MCP3008, 8 channels in total
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data


# Main fucntion of the program 
while True:
    # Read the light and soil value
    light_value = readadc(light)
    light_porc = light_value*100/1023
    soil_value = readadc(soil)
    soil_porc  = (soil_value*100/1023 - 100) * -1
#    print "---------------------------------------"
#    print("Light Value: %d" % light_value)
#    print("Light Porcenture: %d" % light_porc)
#    print("Soil Value: %d" % soil_value)
#    print("Soil Porcenture: %d" % soil_porc)

    # Send it to Thingspeak
    update = urllib.urlopen("https://api.thingspeak.com/update?key=" + write_key + "&field1=" + str(light_porc) 
+ "&field2=" + str(light_value) + "&field3=" + str(soil_porc) + "&field4=" + str(soil_value))


    # Calculate, using Thingspeak, the postion of our servo motor 
    servo_position = urllib.urlopen("https://api.thingspeak.com/channels/" + channel_id + "/fields/5/last.txt").read()
#    print(servo_position)
    if servo_position == "1" and current_position == 0:
        servo.start(7.5)
        current_position = 1
        time.sleep(3)
        servo.stop()
    elif current_position != 0:
        servo.start(2.5)
        current_position = 0
        time.sleep(3)
        servo.stop()
    
    # See if we need to open the relay (water the plant)
    need_water = urllib.urlopen("https://api.thingspeak.com/channels/" + channel_id + "/fields/6/last.txt").read()
    if need_water == "1":
      update = urllib.urlopen("https://api.thingspeak.com/update?key=" + write_key + "&field6=0") 
      GPIO.output(11, GPIO.LOW) # Start the pump
      time.sleep(5)
      GPIO.output(11, GPIO.HIGH) # Stop the pump
        
    #Delay the processing until the next cycle
    time.sleep(delay)
