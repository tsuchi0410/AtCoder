S = []
for i in range(8):
    S.append(input())

alpha = "abcdefgh"
num = "12345678"

ans = ""
for i in range(8):
    for j in range(8):
        if S[i][j] == "*":
            ans += alpha[j]
            ans += num[7 - i]

print(ans)