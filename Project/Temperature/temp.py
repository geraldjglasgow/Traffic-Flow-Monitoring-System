import sys
import Adafruit_DHT
import time

file = open("ambient.log", "a")
while True:
    humidity, temperature = Adafruit_DHT.read_retry(11,14)
    file.write('Temp: ' + repr(temperature) + 'C ' + 'Humidity: ' + repr(humidity) + '%\n')
    time.sleep(60)    
