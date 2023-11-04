S = input()
N = int(input())
S = list(S)

q = set()
for i in range(len(S)):
    if S[i] == "?":
        q.add(i)
        S[i] = "0"

ans = "0b" + "".join(S)
ans = int(ans, 2)

for i in range(len(S)):
    if i in q:
        S[i] = "1"
        l = "0b" + "".join(S)
        l = int(l, 2)
        if l <= N:
            ans = max(ans, l)
        else:
            S[i] = "0"

if ans <= N:
    print(ans)
else:
    print(-1)
