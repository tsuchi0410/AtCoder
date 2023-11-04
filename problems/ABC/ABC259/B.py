import numpy as np
import math

L = list(map(int,input().split()))

s = (math.sin(math.radians(L[2])))
c = (math.cos(math.radians(L[2])))

x2 = L[0]*c - L[1]*s
y2 = L[0]*s + L[1]*c

print(x2,y2)


