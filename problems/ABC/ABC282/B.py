n,m=(int(x) for x in input().split())
s=[]
for i in range(n):
    s.append(input())

ans = 0
for i in range(n):
    for j in range(i+1,n):
        f = 1
        for k in range(m):
            if s[i][k] == 'o' or s[j][k] == 'o':
                pass
            else:
                f = 0
        if f == 1:
            ans += 1
print(ans)