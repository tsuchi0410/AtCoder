N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort(reverse=True)
ans = 0
for i in range(N):
    if K > 0:
        K -= 1
        continue
    else:
        ans += H[i]

print(ans)