import argparse
import time
from server import HttpServer

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Starts up the server.')
    parser.add_argument('host_address', metavar='HOST ADDRESS', help='host address')
    parser.add_argument('-p', '--p', metavar='HOST PORT', help='host port',\
        nargs='?', default='8080', dest='host_port', type=int)
    parser.add_argument('-g', '--g', metavar='GPIO PIN', help='GPIO pin',\
        nargs='?', default='4', dest='gpio_pin', type=int)
    args = parser.parse_args()
    
    host = args.host_address
    port = args.host_port
    server = HttpServer((host, port), args.gpio_pin)
    print time.asctime(), "Server Starts - %s:%s" % (host, port)
    server.start()
    server.stop()
    print time.asctime(), "Server Stops - %s:%s" % (host, port)
