import argparse
import time
import BaseHTTPServer
from server import HttpServer

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Starts up the server.')
    parser.add_argument('host_address', metavar='HOST ADDRESS', help='host address')
    parser.add_argument('-p', '--p', metavar='HOST PORT', help='host port',\
        nargs='?', default='8080', dest='host_port', type=int)
    args = parser.parse_args()
    
    host = args.host_address
    port = args.host_port
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((host, port), HttpServer)
    print time.asctime(), "Server Starts - %s:%s" % (host, port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (host, port)
