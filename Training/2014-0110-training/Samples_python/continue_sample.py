
def lookup(n):
    return n
def valid(n):
    return True
def transform(n):
    return n * 4

table = {}
def test1(container):
    """Demonstrate use of the continue statement."""
    for n in container:
        if n % 2 == 0:
            continue
        value = lookup(n)
        if value not in table:
            continue
        value = transform(value)
        if not valid(value):
            continue
        print value


def test2(container):
    """Show what the above code might look like if we do not use continue."""
    for n in container:
        if n % 2 != 0:
            value = lookup(n)
            if value in table:
                value = transform(value)
                if valid(value):
                    print value
