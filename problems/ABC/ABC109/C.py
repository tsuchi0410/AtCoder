import math
N, X = (int(x) for x in input().split())
x = list(map(int,input().split()))

a = float('inf')

if N == 1:
    print(abs(X - x[0]))
    exit()
    
for i in range(N-1):
    a = min(a, math.gcd(X - x[i], X - x[i+1]))
    
print(a)
        