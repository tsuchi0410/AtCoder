N = int(input())


if N == 1:
    print("1")
    exit()
elif N == 2:
    print("2")
    exit()

ans = [0]*N
ans[0] = 1
ans[1] = 2
ans[2] = 4

for i in range(3,N):
    ans[i] = ans[i-3]+ans[i-2]+ans[i-1]

print(ans[-1])