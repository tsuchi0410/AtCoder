N = int(input())
A = list(map(int,input().split()))

T = [0]*N
T[1] = A[1]

for i in range(2,N):
    T[i] = min(T[i-1]+A[i], T[i-2]+A[i]*2)

print(T[-1])