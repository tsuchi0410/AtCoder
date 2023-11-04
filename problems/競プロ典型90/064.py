N, Q = map(int,input().split())
A = list(map(int,input().split()))
lst = []
for i in range(N - 1):
    lst.append(abs(A[i] - A[i + 1]))
ans = sum(lst)
for _ in range(Q):
    L, R, V = map(int,input(). split())
    L -= 1
    R -= 1
    if L != 0:
        b = lst[L - 1]
        a = abs(A[L - 1] - (A[L] + V))
        ans += a - b
        lst[L - 1] = a
    if R != N - 1:
        b = lst[R]
        a = abs(A[R] + V - A[R + 1])
        ans += a - b
        lst[R] = a
    print(ans)