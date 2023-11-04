n, m = (int(x) for x in input().split())

s = []
for i in range(m):
    c = int(input())
    a = list(map(int,input().split()))
    s.append(set(a))

ans = 0
for i in range(2 ** m):
    l = [i >> j & 1 for j in range(m)]
    now = set()
    for j in range(len(l)):
        if l[j] == 1:
            now = now.union(s[j])
    
    if len(now) == n:
        ans += 1
    
print(ans)