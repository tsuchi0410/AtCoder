N = int(input())
a = list(map(int,input().split()))

a = [0] + a
N += 1

b = [0] * N
for i in range(N - 1, 0, -1):
    p = 0
    if a[i] == 1:
        p += 1
    
    for j in range(i, N + 1, i):
        if j >= N:
            break
        if b[j] == 1:
            p += 1

    b[i] = p % 2

ans = []
for i in range(N):
    if b[i] == 1:
        ans.append(i)

print(len(ans))
print(*ans)