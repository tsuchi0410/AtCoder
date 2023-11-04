import math
import functools
n = int(input())
a = list(map(int,input().split()))

g = functools.reduce(math.gcd, a)
cnt = 0
for i in range(n):
    a[i] //= g
    num = a[i]
    while True:
        if num % 3 == 0:
            num //= 3
            cnt += 1
        elif num % 2 == 0:
            num //= 2
            cnt += 1
        else:
            break
    a[i] = num

if len(set(a)) == 1:
    print(cnt)
else:
    print('-1')
