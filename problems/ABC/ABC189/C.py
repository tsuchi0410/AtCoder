N = int(input())
A = list(map(int,input().split()))

a = 0
for i in range(N):
    b = A[i]
    
    for j in range(i, N):
        
        b = min(b, A[j])
        a = max(a, b * (j - i + 1))

print(a)