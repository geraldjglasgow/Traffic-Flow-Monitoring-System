import subprocess
import time as t

def main():
	while True:
		file = open("cputemp.log","a")
		p = subprocess.Popen(["cat /sys/class/thermal/thermal_zone0/temp"], stdout=subprocess.PIPE, shell=True)
		temp0 = p.stdout.read()
		temp0 = int(temp0)
		temp1 = temp0/1000
		temp2 = temp0/100
		temp3 = temp0/10
		tempm = temp2 % temp1
		tempm2 = temp3 % 10
		str_temp = str(temp1) + "." + str(tempm) + str(tempm2) + "C"
		file.write("%s\n" % str_temp)
		t.sleep(60)

if __name__ == "__main__":
	main()