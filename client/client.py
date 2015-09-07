import RPi.GPIO as GPIO
import time
import urllib2

class Client:
    def __init__(self, server_address, gpio_pin):
        self.server_address = server_address
        self.gpio_pin = gpio_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpio_pin, GPIO.IN)
    def start(self):
        address,port = self.server_address
        current = GPIO.input(self.gpio_pin)
        request = 'http://' + address + ':' + port + '/light?'
        try:
            while 1:
                if GPIO.input(self.gpio_pin) != current:
                    current = GPIO.input(self.gpio_pin)
                    req = reuest
                    if current:
                        req = 'on'
                    else:
                        req = 'off'
                    urllib2.urlopen(req).read()
                    print('Sending network request...')
                else:
                    time.sleep(0.25) 
        except KeyboardInterrupt:
            pass
    def stop(self):
        GPIO.cleanup()    
