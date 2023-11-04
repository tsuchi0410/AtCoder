H, W = map(int, input().split())
S = []
for i in range(H):
    A = list(map(int, input().split()))
    l = []
    for j in range(W):
        if A[j] == 0:
            l.append(".")
        else:
            l.append(chr(A[j] + 64))
    S.append(l)

for i in range(H):
    print(*S[i], sep = "")
    
