n = int(input())
s = list(map(int,input().split()))

l = [0]
for i in range(n):
    l.append(s[i]-sum(l))
    


print(*l[1:])