"""
Synopsis:
    A simple server that responds to a Web request with "pong".
Usage:
    python gevent1.py
Hints:
    - modules gevent and gevent.socket from the gevent prackage
Solution:
    Solutions/gevent1.py
"""

import gevent
from gevent import socket


def handle_pong(sock):
    sock.sendall("HTTP/1.0 200 OK\r\nContent-Length: 5\r\n\r\nPong!\r\n")
    sock.close()


HandlerTable = {
    'pong': handle_pong,
}


def test():
    server = socket.socket()
    server.bind(('localhost', 8070))
    server.listen(500)
    print 'listening on http://localhost:8070/'
    while True:
        try:
            new_sock, address = server.accept()
        except KeyboardInterrupt:
            break
        # handle every new connection with a new coroutine
        handler = HandlerTable['pong']
        gevent.spawn(handler, new_sock)


test()
