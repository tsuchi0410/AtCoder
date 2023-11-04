N,L,R = (int(x) for x in input().split())
A = list(map(int,input().split()))

dp1 = []
dp2 = []
for i in range(N):
    dp1.append([0]*N)
    dp2.append([0]*N)

dp1[0] = A[0] - L
x = dp1[0]
idx = 0
for i in range(1, N):
    dp1[i] = (A[i]-L) + dp1[i-1]
    if x < dp1[i]:
        x = dp1[i]
        idx = i+1

if idx == 0 and x > 0:
    A[0] = L


for i in range(0, idx):
    A[i] = L


dp2[N-1] = A[N-1] - R
y = dp2[N-1]
idy = N-1
for i in range(N-2,-1,-1):
    dp2[i] = (A[i]-R) + dp2[i+1]
    if y < dp2[i]:
        y = dp2[i]
        idy = i-1

if idy == N-1 and y > 0:
    A[N-1] = R

for i in range(N-1, idy,-1):
    A[i] = R


print(sum(A))
