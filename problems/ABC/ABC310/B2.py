N, M = map(int, input().split())
P = []
F = []
for _ in range(N):
    p, c, *f = map(int, input().split())
    P.append(p)
    F.append(set(f))

for i in range(N):
    for j in range(N):
        
        if i == j:
            continue

        if P[i] > P[j] and F[j] >= F[i]:
            print("Yes")
            exit()
        
        if P[i] == P[j] and F[j] >= F[i] and len(F[j]) > len(F[i]):
            print("Yes")
            exit()

print("No")