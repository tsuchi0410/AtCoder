N, D, P = map(int, input().split())
F = list(map(int, input().split()))
F.sort(reverse=True)
L = [0] * (2 * 10**5 + 10)
F += L

S = [0]
for i in range(len(F)):
    S.append(S[i] + F[i])

i = 0
ans = 0
while 1:
    cnt = S[i + D] - S[i]
    if cnt <= P:
        ans += cnt
    else:
        ans += P
    i += D

    if i >= N:
        break

print(ans) 