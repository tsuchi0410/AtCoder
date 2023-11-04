H, W = (int(x) for x in input().split())
A = []
for i in range(H):
    AA = list(map(int,input().split()))
    A.append(AA)


BIT = H + W - 2
cnt = 0
for i in range(2 ** BIT):
    l = [i >> j & 1 for j in range(BIT)]
    
    ans = set()
    ii = 0
    jj = 0
    ans.add(A[ii][jj])

    for j in range(len(l)):
        if l[j] == 1:
            ii += 1
        else:
            jj += 1
        
        if ii >= H or jj >= W:
            break
        else:
            ans.add(A[ii][jj])
    
    if len(ans) == BIT + 1:
        cnt += 1

print(cnt)

