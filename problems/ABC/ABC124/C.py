S = list(input())
for i in range(len(S)):
    S[i] = int(S[i])

cnt = 0
num = S[0]
for i in range(1, len(S)):
    if num == S[i]:
        num ^= 1
        S[i] ^= 1
        cnt += 1
    else:
        num = S[i]

print(cnt)