def base10toM(N, M):
    L = []
    while True:
        x = N % M
        L.append(x)
        N //= M
        if N < M:
            L.append(N)
            break
    L.reverse()
    return L

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    cnt = sum(base10toM(N, 3))
    if cnt <= K <= N:
        if cnt % 2 == K % 2:
            print("Yes")
            continue
    
    print("No")