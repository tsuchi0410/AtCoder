N = int(input())
D = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(101):
        s = str(i + 1) + str(j)
        s = set(s)
        if len(s) == 1 and j <= D[i]:
            ans += 1

print(ans)