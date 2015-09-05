import RPi.GPIO as GPIO

class Client:
    def __init__(self, server_address):
        self.server_address = server_address
