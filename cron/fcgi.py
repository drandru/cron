# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse
import sys

from FastCGIClient import *


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', help='Example: 127.0.0.1', required=True)
    parser.add_argument('-p', '--port', help='Example: 9000', required=True)
    parser.add_argument('-u', '--uri', 
        help='Request uri. Example: /open-graph/v1/frontend/news/item/43466073/', required=True)
    parser.add_argument('-s', '--script-name', help='Example: app.php', required=True)
    parser.add_argument('-d', '--docroot', help='Example: /home/www/path/to/documentroot', required=True)
    parser.add_argument('-q', '--query', help='Query string. Example: page=1&limit=10', default='')
    parser.add_argument('-ra', '--remote-address', help='Remote address', default='172.18.0.2')
    parser.add_argument('-rp', '--remote-port', help='Remote port', default='47604')
    parser.add_argument('-sa', '--server-address', help='Server address', default='172.18.0.6')
    parser.add_argument('-sp', '--server-port', help='Server port', default='172.18.0.6')
    parser.add_argument('-m', '--method', help='Http method', default='GET')
    parser.add_argument('-c', '--content',
        help='Request body (for example on form POST): first_name=john&last_name=doe', default='')
    parser.add_argument('-ct', '--content-type',
        help='Content type (for example on form POST): application/x-www-form-urlencoded', default='')

    return parser.parse_args()


def main():
    args = parse_args()
    print(args)
    client = FastCGIClient(args.host, args.port, 3000, 0)

    request_uri = args.uri

    if args.query:
        request_uri += '?' + args.query
 
    params = {
        'GATEWAY_INTERFACE': 'CGI/1.0',
        'REQUEST_METHOD': args.method,
        'SCRIPT_FILENAME': args.docroot + args.script_name,
        'SCRIPT_NAME': args.script_name,
        'QUERY_STRING': args.query,
        'REQUEST_URI': request_uri,
        'DOCUMENT_ROOT': args.docroot,
        'DOCUMENT_URI': args.script_name,
        'SERVER_SOFTWARE': 'nginx/1.15.7',
        'REMOTE_ADDR': args.remote_address,
        'REMOTE_PORT': args.remote_port,
        'SERVER_ADDR': args.server_address,
        'SERVER_PORT': args.server_port,
        'SERVER_NAME': "localhost",
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'REQUEST_SCHEME': 'http',
        'CONTENT_TYPE': args.content_type,
        'CONTENT_LENGTH': len(args.content) or '',
        'HTTP_HOST': 'local.mos-team.ru',
        'HTTP_USER_AGENT': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0.?HTTP_ACCEPTtext/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    }
    print(client.request(params, args.content))


if __name__ == '__main__':
    main()
