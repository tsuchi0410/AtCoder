import math
R,X,Y = (int(x) for x in input().split())

b = X*X + Y*Y
k = math.sqrt(b) / R

if k < 1:
    print(2)
    exit()

if k - int(k) == 0:
    print(int(k))
else:
    print(int(k+1))

