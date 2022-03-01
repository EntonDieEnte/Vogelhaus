import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep

camera = PiCamera()
PIR_Sensor = 23
LED = 24
i = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_Sensor, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

def sensor(PIR_Sensor):
    global i 
    i = i + 1
    camera.capture('/home/pi/Desktop/bilder/image%s.jpg' % i)
    print('Bewegung erkannt')
    GPIO.output(LED, False)

if __name__ == "__main__":
    try:
        GPIO.add_event_detect(PIR_Sensor, GPIO.RISING, callback=sensor)
        while True:
            sleep(0)

    except KeyboardInterrupt:
        print('beendet')
        GPIO.cleanup
