import sys


def filter(n, fill):
    for line in sys.stdin:
        line = line.rstrip()
        if n == -1:
            line2 = "%s%s" % (line, fill, )
        elif n > len(line):
            line2 = "%s%s" % (line.ljust(n), fill, )
        else:
            line2 = "%s%s%s" % (line[:n], fill, line[n:], )
        #sys.stdout.write("line:  %s\n" % line)
        sys.stdout.write("%s\n" % line2)


def main():
    args = sys.argv[1:]
    n = int(args[0])
    fill = args[1]
    filter(n, fill)


if __name__ == '__main__':
    main()
