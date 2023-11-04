N,L,R = (int(x) for x in input().split())
A = list(map(int,input().split()))

left = [0]*(N+1)
right = [0]*(N+1)

for i in range(1,N+1):
    left[i] = left[i-1] + (A[i-1]-L)

for i in range(N-1,-1,-1):
    right[i] = right[i+1] + (A[i]-R)

for i in range(1, len(left)):
    left[i] = max(left[i],left[i-1])

for i in range(N-1,-1,-1):
    right[i] = max(right[i],right[i+1])

nummax = float('inf')*(-1)

print(left)
print(right)


for i in range(len(left)):
    nummax = max(nummax, left[i]+right[i])

print(sum(A)-nummax)

