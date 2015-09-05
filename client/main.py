import argparse
import time
from client import Client

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Starts up the client.')
    parser.add_argument('server_address', metavar='SERVER ADDRESS', help='server address')
    parser.add_argument('-p', '--port', metavar='SERVER PORT', help='server port',\
        nargs='?', default='8080', dest='server_port', type=int)
    parser.add_argument('-g', '--gpio', metavar='GPIO PIN', help='GPIO pin',\
        nargs='?', default='4', dest='gpio_pin', type=int)
    
    args = parser.parse_args()
    client = Client((args.server_address, args.server_port), args.gpio_pin)
    print time.asctime(), 'Client Starts - %s:%s' % (args.server_address, args.server_port)
    client.start()
    print time.asctime(), 'Client Stops'
    client.stop()
