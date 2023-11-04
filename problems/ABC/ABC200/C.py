from math import factorial

N = int(input())
A = list(map(int,input().split()))

d = {}
for i in range(N):
    if A[i] >= 200:
        x = A[i] % 200         
    else:
        x = A[i]
    
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

ans = 0
for i in d.values():
    if i >= 2:
        ans += factorial(i) / (factorial(2) * factorial(i - 2))

print(int(ans))

        
