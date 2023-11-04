def f(n):
    if n + 1 <= len(S):
        return n
    

S = input()
Q = int(input())
for _ in range(Q):
    t, k = map(int, input().split())
    f(t)