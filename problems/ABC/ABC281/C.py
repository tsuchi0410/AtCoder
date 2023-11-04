n,t = (int(x) for x in input().split())
a = list(map(int,input().split()))

s = [0]
for i in range(n):
    s.append(s[i]+a[i])

s_sum = s[-1]
t %= s_sum

for i in range(len(s)):
    if t <= s[i]:
        print(i, t-s[i-1])
        exit()
