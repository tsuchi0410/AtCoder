S = input()
N = len(S)
ans = 0
for i in range(1, N + 1):
    for j in range(N):
        if j + i == N + 1:
            break
        a = S[j : j + i]
        f = True
        for k in range(len(a)):
            if a[k] != a[len(a) - k - 1]:
                f = False
        if f == True:
            ans = max(ans, len(a))

print(ans)