import copy
N = int(input())
A = list(map(int,input().split()))
A2 = copy.deepcopy(A)
B = []
for i in range(N - 1):
    if A[i] < 0:
        A[i] *= -1
        A[i + 1] *= -1
    B.append(A[i])

B.append(A[-1])
if B[-1] >= 0:
    print(sum(B))
else:
    num = 10**10
    B[-1] *= -1
    for i in range(N):
        if A2[i] < 0:
            A2[i] *= -1
        num = min(num, A2[i])
    print(sum(B) - 2 * num)