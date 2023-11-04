N,M = (int(x) for x in input().split())
D = list(map(int,input().split()))

ans = [False]*(N+1)

for i in range(1,N+1):
    for j in range(M):
        if i == D[j]:
            ans[i] = True
        if i-D[j] >= 0:
            if ans[i-D[j]] == True:
                ans[i] = True

if ans[-1] == True:
    print("Yes")
else:
    print("No")


            
