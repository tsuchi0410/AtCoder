N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

MAXNUM = 1000000
TEST = [0]*MAXNUM

for i in range(N):
    TEST[B[C[i]-1]] += 1

ans = 0
for i in range(N):
    ans += TEST[A[i]]

print(ans)