N, K = map(int,input().split())
if N == 0:
    print(0)
    exit()
for _ in range(K):
    S = str(N)
    num = 0
    S = S[::-1]
    for i in range(len(S)):
        num += int(S[i]) * (8 ** i)

    l = []
    while num != 0:
        p = num % 9
        l.append(p)
        num //= 9

    l.reverse()
    for i in range(len(l)):
        if l[i] == 8:
            l[i] = 5
        l[i] = str(l[i])
    N = "".join(l)
print(N)