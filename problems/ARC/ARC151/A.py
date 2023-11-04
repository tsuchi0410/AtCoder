N = int(input())
S = list(input())
T = list(input())
for i in range(N):
    S[i] = int(S[i])
    T[i] = int(T[i])

cnt = 0
cntS = 0
cntT = 0
for i in range(N):
    if S[i] != T[i]:
        cnt += 1

if cnt % 2 != 0:
    print(-1)
else:
    ans = []
    for i in range(N):
        if S[i] == T[i]:
            ans.append(0)
        else:
            if cntS * 2 == cnt:
                ans.append(T[i])
            elif cntT * 2 == cnt:
                ans.append(S[i])
            elif S[i] == 0:
                cntS += 1
                ans.append(0)
            elif T[i] == 0:
                cntT += 1
                ans.append(0)
    for i in range(N):
        ans[i] = str(ans[i])
    print("".join(ans))
    