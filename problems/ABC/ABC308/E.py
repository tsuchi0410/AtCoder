import bisect
N = int(input())
A = list(map(int, input().split()))
S = input()

M = {}
E = {}
X = {}

for i in range(3):
    M[i] = []
    E[i] = []
    X[i] = []

for i in range(N):
    if S[i] == "M":
        M[A[i]].append(i)
    if S[i] == "E":
        E[A[i]].append(i)
    if S[i] == "X":
        X[A[i]].append(i)

ans = 0
for i in range(N):
    if S[i] == "E":
        m0 = bisect.bisect_left(M[0], i)
        m1 = bisect.bisect_left(M[1], i)
        m2 = bisect.bisect_left(M[2], i)
        x0 = len(X[0]) - bisect.bisect_left(X[0], i)
        x1 = len(X[1]) - bisect.bisect_left(X[1], i)
        x2 = len(X[2]) - bisect.bisect_left(X[2], i)
        if A[i] == 0:
            ans += m0 * x0 * 1
            ans += m0 * x1 * 2
            ans += m0 * x2 * 1
            ans += m1 * x0 * 2
            ans += m1 * x1 * 2
            ans += m1 * x2 * 3
            ans += m2 * x0 * 1
            ans += m2 * x1 * 3
            ans += m2 * x2 * 1
        elif A[i] == 1:
            ans += m0 * x0 * 2
            ans += m0 * x1 * 2
            ans += m0 * x2 * 3
            ans += m1 * x0 * 2
            ans += m1 * x1 * 0
            ans += m1 * x2 * 0
            ans += m2 * x0 * 3
            ans += m2 * x1 * 0
            ans += m2 * x2 * 0
        elif A[i] == 2:
            ans += m0 * x0 * 1
            ans += m0 * x1 * 3
            ans += m0 * x2 * 1
            ans += m1 * x0 * 3
            ans += m1 * x1 * 0
            ans += m1 * x2 * 0
            ans += m2 * x0 * 1
            ans += m2 * x1 * 0
            ans += m2 * x2 * 0
print(ans)