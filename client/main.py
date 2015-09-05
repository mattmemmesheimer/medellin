import argparse
from client import Client

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Starts up the client.')
    parser.add_argument('server_address', metavar='SERVER ADDRESS', help='server address')
    parser.add_argument('-p', '--port', metavar='SERVER PORT', help='server port',\
        nargs='?', default='8080', dest='server_port', type=int)
    
    args = parser.parse_args()
    client = Client((args.server_address, args.server_port))
