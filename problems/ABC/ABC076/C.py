S = input()
T = input()

cnt = []
for i in range(len(S)):
    f = False
    if S[i] == T[0] or S[i] == "?":
        f = True
    
    if f == True:
        j = 0
        while True:
            if i + j >= len(S) or j >= len(T):
                break
            elif S[i + j] == T[j] or S[i + j]  == "?":
                j += 1
            else:
                break
        if j == len(T):
            cnt.append(i)

if len(cnt) == 0:
    print("UNRESTORABLE")
else:
    ans = []
    for c in cnt:
        l = []
        i = 0
        while i < len(S):
            if c != i:
                if S[i] == "?":
                    l.append("a")
                else:
                    l.append(S[i])
                i += 1
            else:
                l.append(T)
                i += len(T)
        ans.append(l)
    for i in range(len(ans)):
        ans[i] = "".join(ans[i])
    ans.sort()
    print(ans[0])