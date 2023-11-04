import math
n = int(input())
p = list(map(int,input().split()))

def f(num):
    l = list(range(101))
    l = l[1:]
    aa = 0
    for i in range(100):
        if l[i] == num:
            return aa
        else:
            aa += math.factorial(i)
            

ans = 0
for i in range(n):
    a = f(p[i])
    ans += a