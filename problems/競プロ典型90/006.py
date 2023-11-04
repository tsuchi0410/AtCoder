N, K = map(int, input().split())
S = input()

# nex[i][c]: 文字列 S の i 文字目以降で最初に文字 c が出現するタイミング (0-indexed)
# 存在しないとき -> c = N
# 文字列が小文字 -> ord(x) - 97
# 文字列が大文字 -> ord(x) - 65
nex = [[N] * 26 for n in range(N + 1)]
 
for i in range(N - 1, -1, -1):
    nex[i][ord(S[i]) - 97] = i
    for c in range(26):
        nex[i][c] = min(nex[i][c], nex[i + 1][c])

ans = []
i = 0
while K:
    for c in range(26):
        if N - nex[i][c] >= K:
            ans.append(chr(c + 97))
            i = nex[i][c] + 1
            K -= 1
            break
print("".join(ans))
