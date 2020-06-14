from random import random
from math import sqrt
import time
DARTS = 1200
hits = 0
time.process_time()
for i in range(1,DARTS):
    x, y = random(), random()
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("pi value is %s" % pi)
print("run time is %-5.5ss" % time.process_time())
