N, K = (int(x) for x in input().split())
A = list(map(int,input().split()))

A = set(A)
for i in range(K):
    if not i in A:
        print(i)
        exit()

print(K)