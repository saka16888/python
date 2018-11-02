#!/usr/bin/python

"""
Synopsis:
    Implement an XML-RPC server that response to (serves) several
    mathematical functions, for example pow, sqrt, etc.
Usage:
    python xmlrpcserver1.py
Hints:
    - module SimpleXMLRPCServer in the Python standard library.
Solution:
    Solutions/xmlrpcserver1.py
"""

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


def adder_function(x, y):
    return x + y


class MyFuncs:
    def div(self, x, y):
        return x // y


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


def run_server():
    # Create server
    server = SimpleXMLRPCServer(("localhost", 8000),
                                requestHandler=RequestHandler)
    server.register_introspection_functions()

    # Register pow() function; this will use the value of
    # pow.__name__ as the name, which is just 'pow'.
    server.register_function(pow)

    # Register a function under a different name
    server.register_function(adder_function, 'add')

    # Register an instance; all the methods of the instance are
    # published as XML-RPC methods (in this case, just 'div').
    server.register_instance(MyFuncs())

    # Run the server's main loop
    server.serve_forever()


def main():
    run_server()


if __name__ == '__main__':
    main()
