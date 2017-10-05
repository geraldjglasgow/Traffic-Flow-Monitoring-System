# PowerBoost 1000c

##### When using a manual switch:
- Left pin to USB or BAT (to turn on/off charging or battery)
- Middle pin to EN
- R: GND

## PowerBoost 1000c detecting low power on Raspberry Pi
##### Connect the LBO pin to pin 21 on the RPi, then below script will check every 60 seconds to see if the battery has dropped below 3.2V. If it does this triggers a safe shutdown.

    import PRi.GPIO as g
    import time as t
    import os
    
    g.setup(g.BCM)
    g.setup(21, g.IN, pull_up_down=g.PUD_UP)
    
    while True:
    if g.input(21) == g.LOW:
        print("pin is low (Battery is low)")
        os.system('sudo shutdown -h now')
        t.sleep(60)
    else:
        print("pin is high (Battery has charge)")
        t.sleep(60)




