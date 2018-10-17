import threading
import time

def read_scanner(buff, flag):
  fp = open("/dev/hidraw2", "rb")
  while flag >= 0:
    if flag > 0:
      buff.append(fp.read(1))
    time.sleep(0.001)
  fp.close()

buff = bytearray()
flag = 1
t = threading.Thread(target=read_scanner, args=(buff, flag))
t.start()
N = 8

try:
  while True:
    if len(buff) >= N:
      flag = 0 # stop adding
      print([i for i in buff[:N]],'\n')
      buff = buff[N:]
      flag = 1
    time.sleep(0.001)

except KeyboardInterrupt:
  flag = -1
