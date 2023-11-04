N = int(input())
ans = 10 ** 18
for a in range(1, int(N ** 0.5) + 1):
    if N % a == 0:
        b = N // a
        ans = min(ans, max(len(str(a)), len(str(b))))
print(ans)