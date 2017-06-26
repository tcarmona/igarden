#!/usr/bin/python
 
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
channel_id = 293365


# Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)
 
# Connect with thingspeak magic
channel = thingspeak.Channel(channel_id, read_key, write_key)


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
    print "---------------------------------------"
    print("Light Value: %d" % light_value)
    print("Light Porcenture: %d" % light_porc)
    print("Soil Value: %d" % soil_value)
    print("Soil Porcenture: %d" % soil_porc)

    # Send it to Thingspeak
    print(channel.get())
    update = urllib.urlopen("https://api.thingspeak.com/update?key=" + write_key + "&field1=" + str(light_porc) 
+ "&field2=" + str(light_value) + "&field3=" + str(soil_porc) + "&field4" + str(soil_value))

    time.sleep(delay)
