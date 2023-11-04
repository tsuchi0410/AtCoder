N = int(input())
C = []
S = []
F = []
for i in range(N - 1):
    c, s, f = map(int,input().split())
    C.append(c)
    S.append(s)
    F.append(f)

if N == 1:
    print(0)
    exit()

for f in range(N - 1):
    time = S[f] + C[f]
    for i in range(f + 1, N - 1):
        if S[i] > time:
            time = S[i] + C[i]
        else:
            if (time - S[i]) % F[i] == 0:
                time += C[i]
            else:
                x = (time - S[i]) // F[i]
                d = F[i] * (x + 1) - (time - S[i])
                time += d + C[i]
    print(time)
print(0)