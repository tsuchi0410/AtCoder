N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
grundy = [0, 0, 1, 1, 2]
x = 0
for i in range(N):
    x ^= grundy[A[i] % 5]
if x != 0:
    print("First")
else:
    print("Second")