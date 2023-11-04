N, H, W = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())
    A[i] -= 1
    B[i] -= 1
x = 0
for i in range(N):
    x ^= A[i]
    x ^= B[i]
if x != 0:
    print("First")
else:
    print("Second")