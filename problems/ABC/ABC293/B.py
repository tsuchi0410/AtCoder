N = int(input())
A = list(map(int,input().split()))

l = [False] * N
ans = []
for i in range(N):
    if l[i] == False:
        if l[A[i]-1] == False:
            l[A[i]-1] = True

for i in range(N):
    if l[i] == False:
        ans.append(i+1)

print(len(ans))
print(*ans)