H, W, N, M = (int(x) for x in input().split())
akari = []
for i in range(N):
    A, B = map(int, input().split())
    akari.append([A, B])

bk = []
for i in range(M):
    C, D = map(int, input().split())
    bk.append([C, D])

ans = 0
for i in range(H):
    for j in range(W):
        