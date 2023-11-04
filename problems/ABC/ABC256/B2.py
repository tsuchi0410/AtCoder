N = int(input())
A = list(map(int,input().split()))

cnt = 0
l = [1,0,0,0]
for i in range(N):
    l[0] = 1
    
    for j in range(3,-1,-1):

        if l[j] == 1:
            if j + A[i] > 3:
                cnt += 1
                l[j] = 0
            else:
                l[j+A[i]] = 1
                l[j] = 0
    
print(cnt)