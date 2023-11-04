N, H, X = map(int, input().split())
P = list(map(int, input().split()))
ans = 10**18
num = 0
for i in range(N):
    if P[i] + H >= X:
        if ans > P[i] + H:
            ans = P[i] + H
            num = i + 1
print(num)