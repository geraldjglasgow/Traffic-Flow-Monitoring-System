There have been 3 UPS untis used throughout the course of this project.

1. two capacitors, where once the power is cut from a LiPo battery, 
the capacitors can keep the raspberry pi alive for 25 seconds. In this time the pi is shutdown safely. This was a temporary solution while finding some actual hardware.


https://www.amazon.com/Makerfocus-Raspberry-2500mAh-Lithium-Battery/dp/B01MQYX4UX
2. Makerfocus UPS hat. This UPS sits on top of the pi, doesn't affect GPIO expansion, uses i2c to read voltage.
The following are issues faced with this solution: very small power button, doesnt allow compact case, 
doesnt allow hot swapping battery (UPS must be power cycled).

3. The final solution was the power-boost 1000c. It provides all capablility of the previous
solutions and addresses all issues. 