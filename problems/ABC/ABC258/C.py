N, Q = (int(x) for x in input().split())
S = input()

S = list(S)
h = 0
for i in range(Q):
    t, x = (int(x) for x in input().split())

    if t == 1:
        h += x
        if h >= N:
            h -= N
    if t == 2:
        print(S[x-1-h])
    