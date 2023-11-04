S = str(input())
T = str(input())

NS = len(S)

def a(l):
    l2 = []
    for d in l:
        for i in range(len(d)-1):
            if d[i] == d[i+1]:
                l2.append(d[:i] + d[i] + d[i:])
    return l2

ans = [S]

while len(ans[-1]) <= len(T)-1:
    ans = list(set(ans))
    ans = a(ans)
    

if T in ans:
    print("Yes")
else:
    print("No")

