N, K = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))

L1 = set()
for i in range(N):
    for j in range(N):
        L1.add(A[i] + B[j])

L2 = set()
for i in range(N):
    for j in range(N):
        L2.add(C[i] + D[j])

L1 = list(L1)
for i in L1:
    if K - i in L2:
        print("Yes")
        exit()

print("No")
