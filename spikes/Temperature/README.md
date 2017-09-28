This is a spike for measuring cpu temperature and using a DHC_11 module to measure current
ambient temperature and humidity.

The raspberry pi's cpu temp can be read and parsed into degrees celsius.

    while true                                                      # run until stopped
    do
    
	    cpuTemp0=$(cat /sys/class/thermal/thermal_zone0/temp)       # 23.3432 celsius is read as 233432    
	    cpuTemp1=$(($cpuTemp0/1000))                                # here we obtain the 10's place
	    cpuTemp2=$(($cpuTemp0/100))                                 # getting 1's place
	    cpuTemp3=$(($cpuTemp0/10))                                  # helping getting hundredths place
	    cpuTempM=$(($cpuTemp2 % $cpuTemp1)) # getting tenths place
	    cpuTempM2=$(($cpuTemp3 % 10))                               # getting hundredths place
	    echo $cpuTemp1"."$cpuTempM$cpuTempM2"C" >> /home/pi/Desktop/Project/Temperature/cputemp.txt # write to file
	    sleep 60                                                    # take temp every 60 seconds
    done
    

When using the DHC_11 module 

    import sys
    import Adafruit_DHT
    import time

    file = open("temp.txt", "a")
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(11,14) # reads DHC_11 module from pin 14
        file.write('Temp: ' + repr(temperature) + 'C ' + 'Humidity: ' + repr(humidity) + '%\n')
        time.sleep(60)    
