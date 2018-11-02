import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--rpm", type = int, default=0, help="set fan rpm")
parser.add_argument("--fan_percent", type = int , default=0, help="set fan rpm percent")
args = parser.parse_args()
print("%d , %d" % (args.rpm, args.fan_percent))
