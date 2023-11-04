n, k = (int(x) for x in input().split())
s = []
for i in range(n):
    ss = input()
    s.append([i, ss])

s.sort()
ans = []
for i in range(k):
    ans.append(s[i][1])

ans.sort()
for i in range(k):
    print(ans[i])