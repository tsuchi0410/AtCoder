H, W, K = map(int, input().split())
C = list(input() for _ in range(H))

NUM = H
NUM2 = W
ans = 0
for i in range(2 ** NUM):
    l = [i >> j & 1 for j in range(NUM)]
    for j in range(2 ** NUM2):
        l2 = [j >> k & 1 for k in range(NUM2)]
        cnt = 0
        for k in range(H):
            for m in range(W):
                if l[k] == 1 and l2[m] == 1 and C[k][m] == "#":
                    cnt += 1
        if cnt == K:
            ans += 1
print(ans)
