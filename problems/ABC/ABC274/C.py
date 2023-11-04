n = int(input())
a = list(map(int, input().split()))

l = [0] * (2*n+2)
for i in range(n):
    l[(i+1)*2] = l[a[i]] + 1
    l[(i+1)*2+1] = l[a[i]] + 1

print(*l[1:])