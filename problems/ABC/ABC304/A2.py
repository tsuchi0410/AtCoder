N = int(input())
S = []
A = []
for _ in range(N):
    s, a = map(str,input().split())
    a = int(a)
    S.append(s)
    A.append(a)

i = A.index(min(A))
ans = S[i:] + S[:i]
for s in ans:
    print(s)