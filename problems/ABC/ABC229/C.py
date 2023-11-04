N, W = map(int, input().split())
L = []
for i in range(N):
    A, B = map(int, input().split())
    L.append([A, B])
L.sort(reverse=True)
ans = 0
for k, v in L:
    if v <= W:
        W -= v
        ans += k * v
    else:
        ans += k * W
        break
print(ans)