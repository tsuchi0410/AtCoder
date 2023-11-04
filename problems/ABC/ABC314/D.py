N = int(input())
S = list(input())
Q = int(input())
query = []
last = 0
for _ in range(Q):
    t, x, c = map(str, input().split())
    t = int(t)
    x = int(x)
    query.append([t, x, c])
    if t == 2 or t == 3:
        last = [_, t]

if last == 0:
    for t, x, c in query:
        S[x - 1] = c
else:
    f = False
    for i in range(Q):
        t, x, c = query[i]
        if t == 1:
            S[x - 1] = c
        else:
            if i < last[0]:
                continue
            else:
                if f == True:
                    continue
                else:
                    if t == 2:
                        for j in range(N):
                            S[j] = S[j].lower()
                    elif t == 3:
                        for j in range(N):
                            S[j] = S[j].upper()

print("".join(S))