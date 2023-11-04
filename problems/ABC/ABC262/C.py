import math
N = int(input())
A = list(map(int,input().split()))
#X, Y, Z = (int(x) for x in input().split())

c = 0
d = 0

for i in range(N):
    if A[i] == i+1:
        c += 1
    elif i+1 == A[A[i]-1]:
        d += 1


ans = (c*(c-1))/2 + (d/2)

print(int(ans))
