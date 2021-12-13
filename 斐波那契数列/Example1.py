import time

a, b = 0, 1
while 1:
    a, b = b, b + a
    print(a)
    time.sleep(0.1)
