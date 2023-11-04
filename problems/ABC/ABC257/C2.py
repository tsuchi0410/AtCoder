n = int(input())
s = str(input())
w = list(map(int,input().split()))

l = []
for i in range(n):
    l.append([w[i], s[i]])

l = sorted(l)
# print(l)

cnt = s.count('1')
ans = cnt
for i in range(n):
    
    if l[i][1] == '0':
        cnt += 1
    else:
        cnt -= 1
    
    if i == n-1:
        ans = max(ans, cnt)
        break
    
    if l[i][0] != l[i+1][0]:
        ans = max(ans, cnt)

print(ans)