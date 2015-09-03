import BaseHTTPServer
import RPi.GPIO as GPIO
import urlparse

class HttpServer:
    def __init__(self, server_address, gpio_pin):
        HttpServerHandler.gpio_pin = gpio_pin
        self.gpio_pin = gpio_pin
        self.server_address = server_address
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpio_pin, GPIO.OUT)
        GPIO.output(gpio_pin, False)
    def start(self):
        server = BaseHTTPServer.HTTPServer(self.server_address, HttpServerHandler)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
    def stop(self):
        GPIO.output(self.gpio_pin, False)
        GPIO.cleanup()

class HttpServerHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        
        if parsed_path.path == '/':
           self.handleIndex()
        elif parsed_path.path == '/light':
           self.handleLight()
    def handleIndex(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>Server Test</title></head>")
        self.wfile.write("<body><h1>Server Test</h1><p>Your server is working.</p>")
        self.wfile.write("<b>Pin: </b>" + str(self.gpio_pin))
        self.wfile.write("<br/><b>Path: </b>" + self.path)
        self.wfile.write("</body></html>")
    def handleLight(self):
        parsed_path = urlparse.urlparse(self.path)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        val = False
        valid = False
        if parsed_path.query == 'on':
            val = True
            valid = True
        elif parsed_path.query == 'off':
            val = False
            valid = True
        if valid:
            GPIO.output(self.gpio_pin, val)
        self.wfile.write('<html><body><h1>Light</h1>')
        self.wfile.write(parsed_path.query + '</body></html>')
