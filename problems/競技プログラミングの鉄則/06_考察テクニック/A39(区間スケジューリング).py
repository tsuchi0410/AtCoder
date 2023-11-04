N = int(input())
v = [0] * N
for i in range(N):
    L, R = map(int, input().split())
    v[i] = [L, R]
v.sort(key=lambda x: x[1])
x = v[0][1]
ans = 1
for i in range(N - 1):
    if v[i + 1][0] < x:
        continue
    x = v[i + 1][1]
    ans += 1
print(ans)