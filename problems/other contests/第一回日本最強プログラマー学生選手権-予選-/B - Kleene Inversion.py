N, K = map(int,input().split())
A = list(map(int,input().split()))
MOD = 10**9 + 7

ans = 0
all = 0
right = 0
for i in range(N):
    for j in range(N):
        if i > j:
            if A[i] > A[j]:
                all += 1
        if i == j: continue
        if i < j:
            if A[i] > A[j]:
                right += 1
                all += 1

ans = right * K + all * (K) * (K-1) // 2
print(ans % MOD)

