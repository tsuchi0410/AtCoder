N = int(input())
C = list(map(int,input().split()))

C = sorted(C)

ans = 1
cnt = 0
for i in range(N):
    ans *= (C[i]-cnt)
    ans %= 10**9 + 7
    cnt += 1

print(ans)