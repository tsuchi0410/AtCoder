n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort(); b.sort()
sum = 0
for i in range(n):
    sum += abs(a[i] - b[i])

print(sum)