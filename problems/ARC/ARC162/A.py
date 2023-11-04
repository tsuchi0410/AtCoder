T = int(input())
for _ in range(T):
    N = int(input())
    P = list(map(int,input().split()))
    L = []
    for i in range(N):
        L.append([P[i], i + 1])
    L.sort()
    print(L)