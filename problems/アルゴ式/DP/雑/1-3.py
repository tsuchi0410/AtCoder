N = int(input())

if N == 1:
    print("1")
    exit()

ans = [0]*N
ans[0],ans[1] = 1,2
for i in range(2,N):
    ans[i] = ans[i-2] + ans[i-1]
print(ans[-1])
