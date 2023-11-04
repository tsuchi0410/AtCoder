N = int(input())
ans = 0
for A in range(1, int(N**(1/3)) + 10):
    for B in range(A, N + 1):
        C = N // (A * B)
        if C < B:
            break
        ans += (C - B) + 1
print(ans)