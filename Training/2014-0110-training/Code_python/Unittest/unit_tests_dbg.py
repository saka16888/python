DEBUG = True


def dbgprint(msg):
    """Print a message only if global DEBUG is True.
    """
    if DEBUG:
        print msg
