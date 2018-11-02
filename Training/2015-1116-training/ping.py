import re

def parse_ping(output):
    pat = r'(\d+) packets transmitted, (\d+) packets received, ([0-9.]+)% packet loss'
    mo = re.search(pat, output)
    if mo is None:
        raise NoMatch(pat, output)
    transmitted, received, loss_rate = mo.groups()
    print("transmitted = %d , received %d, loss_rate = %d",transmitted,received, loss_rate)
    if int(loss_rate) <= 50 :
        return True
    else:
        return False
    #return PingResult(int(transmitted), int(received), float(loss_rate))

if __name__ == "__main__":
    output = '''Pinging 1.1.1.2 with 0 bytes of data:

            Reply From 1.1.1.1: Destination Unreachable.
            Reply From 1.1.1.2: icmp_seq = 1. time= 2 msec.
            Reply From 1.1.1.2: icmp_seq = 2. time= 1 msec.

            ----1.1.1.2 PING statistics----
            3 packets transmitted, 2 packets received, 33% packet loss
            round-trip (msec) min/avg/max = <1/2/2'''
    print(parse_ping(output))

