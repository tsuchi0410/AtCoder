N,M = (int(x) for x in input().split())
A = list(map(int,input().split()))

T = [10000000000]*N
T[0] = 0

for i in range(1,N):
    for j in range(1,M+1):
        if i-j >= 0:
            T[i] = min(T[i], T[i-j]+A[i]*j)

print(T[-1])