import sys

fp = open("/dev/hidraw2", "rb")

try:
    while True:
        buffer = fp.read(8)
        for c in buffer:
            if ord(c) > 0:
                print ord(c)
                print "\n" 

except KeyboardInterrupt:
    fp.close()
