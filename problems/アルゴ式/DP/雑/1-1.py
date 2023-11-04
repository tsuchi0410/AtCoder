N, X, Y = (int(x) for x in input().split())

ans = [0]*N
ans[0] = X
ans[1] = Y
for i in range(2,N):
    ans[i] = (ans[i-2]+ans[i-1])%100

print(ans[-1])