N,M = (int(x) for x in input().split())
A = list(map(int,input().split()))

T = [10000000000]*N
T[0] = 0
for i in range(1,N):
    x = 1
    while(1):
        T[i] = min(T[i], T[i-x] + A[i]*x)
        if x == M:
            break
        x += 1

print(T[-1])