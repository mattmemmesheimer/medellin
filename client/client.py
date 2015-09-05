import RPi.GPIO as GPIO
import time

class Client:
    def __init__(self, server_address, gpio_pin):
        self.server_address = server_address
        self.gpio_pin = gpio_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpio_pin, GPIO.IN)
    def start(self):
        try:
            while 1:
                if GPIO.input(self.gpio_pin):
                    # send off network call
                    print('Sending network request...')
                else:
                    time.sleep(0.25) 
        except KeyboardInterrupt:
            pass
    def stop(self):
        GPIO.cleanup()    
