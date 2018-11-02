#!/usr/bin/env python

"""
Synopsis:
    - Implement a class that can be initialized with a to-address, and
      can send messages to that address.
    - Implement a "factory" function that creates an instance of the above
      class.
    - Implement a helper function that uses the above class to send messages.
    - Repeat:
        - Prompt user for subject and body.
        - Send email given fixed from and to addresses.
Usage:
    python send_mail.py
Hints:
    - smtplib module in the Python standard library
    - raw_input built-in function
"""

import sys
import smtplib


class MailHandler(object):
    def __init__(self, fromaddr, toaddr):
        self.fromaddr = fromaddr
        self.toaddrs = [toaddr]

    def send_mail(self):
        server = smtplib.SMTP('localhost')
        #server.set_debuglevel(1)
        server.sendmail(self.fromaddr, self.toaddrs, self.body)
        server.quit()

    def get_subject(self):
        self.subject = raw_input("Subject: ").strip()
        return self.subject

    def get_body(self):
        msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % (
            self.fromaddr,
            ", ".join(self.toaddrs),
            self.subject, )
        print "Enter message, end with ^D (Unix) or ^Z (Windows):"
        while True:
            try:
                line = raw_input()
            except EOFError:
                break
            if not line:
                break
            msg = '%s\n%s' % (msg, line, )
        self.body = msg
        return self.body


def make_handler(fromaddr, toaddr):
    handler = MailHandler(fromaddr, toaddr)
    return handler


def send_mail(handler, subject, body):
    handler.subject = subject
    handler.body = body
    handler.send_mail()


def test1():
    """Test using factory and helper functions."""
    args = sys.argv[1:]
    if len(args) != 0:
        sys.exit(__doc__)
    handler = make_handler(
        'dkuhlman@davekuhlman.org',
        'dkuhlman@davekuhlman.org',
        )
    while True:
        subject = handler.get_subject()
        if not subject:
            break
        body = handler.get_body()
        send_mail(handler, subject, body)


def test2():
    """Test using class directly."""
    args = sys.argv[1:]
    if len(args) != 0:
        sys.exit(__doc__)
    handler = MailHandler(
        'dkuhlman@davekuhlman.org',
        'dkuhlman@davekuhlman.org',
        )
    while handler.get_subject():
        handler.get_body()
        handler.send_mail()


if __name__ == '__main__':
    test1()
