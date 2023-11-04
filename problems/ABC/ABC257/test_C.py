n = int(input())
S = input()
W = list(map(int, input().split()))

ws = []
adcount = 0
for i in range(n):
    ws.append([W[i], int(S[i])])
    if ws[i][1] == 1:
        adcount += 1

ws = sorted(ws)
#
print(ws)
ans = []
ans.append(adcount)
for i in range(n):
    if ws[i][1] == 1:
        adcount -= 1
    else:
        adcount += 1

    if i < n-1:
        if ws[i][0] != ws[i+1][0]:      
            ans.append(adcount)
    else: ans.append(adcount)
print(max(ans))






