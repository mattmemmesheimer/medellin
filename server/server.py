import BaseHTTPServer

class HttpServer(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Server Test</title></head>")
        s.wfile.write("<body><h1>Server Test</h1><p>Your server is working.</p>")
        s.wfile.write("</body></html>")
