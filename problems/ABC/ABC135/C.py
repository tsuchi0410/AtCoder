# 貪欲的に考える

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

B.append(0)
ans = min(B[0], A[0])
B[0] -= ans

for i in range(1, N + 1):
    buf = min(A[i],B[i-1]+B[i])
    if buf > B[i-1]:
        B[i] = B[i] - (buf - B[i-1]) 
    ans += buf

print(ans)