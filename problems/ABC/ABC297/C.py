H, W = map(int,input().split())
S = [input() for _ in range(H)]

ans = []
for i in range(H):
    ans.append(S[i].replace("TT", "PC"))

for i in range(H):
    print(*ans[i], sep = "")