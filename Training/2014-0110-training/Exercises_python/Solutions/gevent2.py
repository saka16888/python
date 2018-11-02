#!/usr/bin/python
"""
Synopsis:
    A REST-ful HTTP server app that response to the following commands:
        - "/" or "/help" --> display command help
        - "/ping"        --> display "pong"
        - "/chocolate"   --> display "vanilla"
        - "/sugar"       --> display "spice"
    Implement your "Web app" with gevent.
Usage:
    python gevent2.py
Resources:
    Comparison of asynchronous servers:
        http://nichol.as/asynchronous-servers-in-python
    Gevent homepage:
        http://gevent.org/
"""

from gevent import wsgi


Help_info = """
<html>
    <head>
        <title>Gevent Web handler demo</title>
    </head>
    <body>
        <p>Commands:</p>
        <ul>
            <li>help</li>
            <li>ping</li>
            <li>chocolate</li>
            <li>sugar</li>
        </ul>
    </body>
</html>
"""


def handle_help(env):
    return [Help_info]


def handle_ping(env):
    return ["<b>pong</b>"]


def handle_chocolate(env):
    return ["<b>vanilla</b>"]


def handle_sugar(env):
    return ["<b>spice</b>"]


HandlerTable = {
    '/': handle_help,
    '/help': handle_help,
    '/ping': handle_ping,
    '/chocolate': handle_chocolate,
    '/sugar': handle_sugar,
}


def simple_web_app(env, start_response):
    #import pdb; pdb.set_trace()
    path_info = env['PATH_INFO']
    handler = HandlerTable.get(path_info)
    if handler is not None:
        start_response('200 OK', [('Content-Type', 'text/html')])
        content = handler(env)
        return content
    else:
        start_response('404 Not Found', [('Content-Type', 'text/html')])
        return ['<h1>Not Found</h1>']


def start_server():
    print 'Serving on 8088...'
    wsgi.WSGIServer(('', 8088), simple_web_app).serve_forever()


def main():
    start_server()


if __name__ == '__main__':
    main()
