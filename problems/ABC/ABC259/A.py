L = list(map(int,input().split()))

if L[2]-L[1] > 0:
    ans = L[3] - L[4]*(L[2]-L[1])
else:
    ans = L[3]

print(ans)