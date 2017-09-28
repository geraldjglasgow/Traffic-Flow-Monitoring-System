while true
do
	cpuTemp0=$(cat /sys/class/thermal/thermal_zone0/temp)
	cpuTemp1=$(($cpuTemp0/1000))
	cpuTemp2=$(($cpuTemp0/100))
	cpuTemp3=$(($cpuTemp0/10))
	cpuTempM=$(($cpuTemp2 % $cpuTemp1))
	cpuTempM2=$(($cpuTemp3 % 10))
	echo $cpuTemp1"."$cpuTempM$cpuTempM2"C" >> /home/pi/Desktop/Project/Temperature/cputemp.txt
	sleep 60
done