import BaseHTTPServer

class HttpServer:
    def __init__(self, server_address, gpio_pin):
        HttpServerHandler.gpio_pin = gpio_pin
        self.server_address = server_address
    def start(self):
        server = BaseHTTPServer.HTTPServer(self.server_address, HttpServerHandler)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass

class HttpServerHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>Server Test</title></head>")
        self.wfile.write("<body><h1>Server Test</h1><p>Your server is working.</p>")
        self.wfile.write("<b>Pin: </b>" + str(self.gpio_pin))
        self.wfile.write("</body></html>")
