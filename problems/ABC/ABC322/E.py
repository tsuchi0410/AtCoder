N, K, P = map(int, input().split())
C = [0] * N
A = [0] * N
for i in range(N):
    C[i], *A[i] = map(int, input().split())

num = 55560
dp = [[0] * num for _ in range(N)]
for i in range(N):
    ai = 0
    for j in range(len(str(ai))):
        ai += len(str(ai))
                   
    for j in range(num):
        