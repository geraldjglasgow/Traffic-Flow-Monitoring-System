import picamera
import datetime as dt
import time
import RPi.GPIO as GPIO

pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

time.sleep(30)
with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.framerate = 15
    camera.start_preview()
    camera.annotate_background = picamera.Color('black')
    camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    camera.start_recording(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+ '.h264')
    start = dt.datetime.now()
    try:
        while True:
            button_state = GPIO.input(pin)
            camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            camera.wait_recording(0.2)
            if button_state == False:
                camera.stop_preview()
                camera.stop_recording()
    except:
        GPIO.cleanup()

#Source: http://picamera.readthedocs.io/en/release-1.10/recipes1.html
#To see video: omxplayer filename.h264