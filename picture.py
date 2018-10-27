import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from time import sleep

import uuid

unique_filename = str(uuid.uuid4())+'.jpg'

SENSOR_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

def mein_callback(channel):
    print('There was a movement! now? make a picture, save it on the internet')

    camera = PiCamera()
    camera.start_preview()
    sleep(1)
    camera.capture('/tmp/' + unique_filename)
    camera.stop_preview()
try:
    GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=mein_callback)
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    print "Now stoping the app"
GPIO.cleanup()


