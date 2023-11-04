# 双対を考える

N = int(input())
B = list(map(int,input().split()))

A = [0] * N
A[0] = B[0]
B.append(B[N-2])
for i in range(1, N):
    A[i] = min(B[i-1],B[i])
    

print(sum(A))
