N = int(input())

ans = [0]*(N+1)
ans[0] = 1

for i in range(1,N+1):
    if i-3 >= 0:
        ans[i] += ans[i-3]
    if i-2 >= 0:
        ans[i] += ans[i-2]
    if i-1 >= 0:
        ans[i] += ans[i-1]

print(ans)