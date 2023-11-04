n, m = (int(x) for x in input().split())
a = list(map(int,input().split()))

s = [0]
for i in range(n):
    s.append(s[i] + a[i])

# 初期値
num = 0
for i in range(m):
    num += (i+1) * a[i]
    
if n == m:
    print(num)
    exit()
    
ans = -1 * float('inf')
for i in range(n):
    
    if m + i < n:
        diff = s[m+i] - s[i] - a[m+i] * m
        num -= diff
        ans = max(ans, num)
        
print(ans)
