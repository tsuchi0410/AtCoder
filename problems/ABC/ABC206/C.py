N = int(input())
A = list(map(int,input().split()))

A = sorted(A)

l = []
cnt = 0
for i in range(1,N):
    if A[i-1] == A[i]:
        cnt += 1
    else:
        l.append(cnt+1)
        cnt = 0

l.append(cnt+1)       
x = N*(N-1)/2

y = 0
for i in range(len(l)):
    if l[i] >= 2:
        y += l[i]*(l[i]-1)/2

print(int(x-y))