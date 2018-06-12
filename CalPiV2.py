#CalPiV2.py

from random import random
from time import perf_counter

hits = 0
DARTS = 1000*1000
start = perf_counter()
for i in range(DARTS):
    x,y = random(),random()
    dist = pow(x**2+y**2,0.5)
    if dist <= 1:
        hits += 1
pi = 4 * (hits/DARTS)

print ("圆周率的值:{}".format(pi))
print ("程序运行的时间为:{:.5f}s".format(perf_counter()-start))
