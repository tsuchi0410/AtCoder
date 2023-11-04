N = int(input())
A = list(map(int, input().split()))
A.sort()

s = A[0]
for i in range(1, N):
    if s + 1 == A[i]:
        s = A[i]
        continue
    print(s + 1)
    exit()