N, X = map(int,input().split())
A = list(map(int,input().split()))

d = {}
for i in range(N):
    d[A[i]] = i
for i in range(N):
    if A[i] - X in d:
        print("Yes")
        exit()
print("No")