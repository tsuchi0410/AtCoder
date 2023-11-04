N, X = map(int, input().split())
A = list(map(int, input().split()))

A.insert(0, -1)
c = 0
while X != 0:
    
    c += 1
    X = A[X]
    
print(c)