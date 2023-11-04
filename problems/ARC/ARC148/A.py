import math

N = int(input())
A = list(map(int,input().split()))

if N == 2:
    r = A[1]-A[0]
    if  r == 1:
        print('2')
        exit()
    else:
        print('1')
        exit()

A = sorted(A)
m = float('inf')
for i in range(N-2):
    r = math.gcd(A[i+2]-A[i+1], A[i+1]-A[i])
    if r >= 2:
        m = min(m, r)
        
b = A[0] % m
for i in range(N):
    b2 = A[i] % m
    if b != b2:
        print('2')
        exit()
    

print('1')