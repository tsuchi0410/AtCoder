n = int(input())
a = list(map(int,input().split()))
s = [0]
for i in range(n):
    s.append(s[i]+a[i])

print(s)