import re

# a1 = [tmp for tmp in input().strip().split(" ")]
# t1=a1[0]

def time_conversion(tm):
    pattern=r'(\d+)\:(\d+):(\d+)(\w+)'
    r1 = re.findall(pattern, tm)
    r2 = re.search(pattern, tm)
    if r2:
        print("Search group ",
              r2.group(0),r2.group(1),
              r2.group(2),r2.group(3),
              r2.group(4))
        print(r2.groups())
    if r1:
        print("pattern = %r, r1 = %r" % (pattern,r1))
        hr = int(r1[0][0])
        if (r1[0][3].upper() == "PM") :
            if (hr != 12):
                hr = (hr+12) % 24
        elif (hr == 12):
            hr = 0
        print("%02d:%s:%s"% (hr,r1[0][1],r1[0][2]))

t1= "12:05:45PM"
#t1= "07:05:45am"
# t1= "12:45:54AM"
# t1= "12:45:54AM"
t1= ["12:05:45PM",
    "1:05:45pm",
    "07:05:45am",
    "12:45:54AM"]

if __name__ == '__main__':
    for t in t1:
        time_conversion(t)





