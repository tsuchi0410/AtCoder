l, r = (int(x) for x in input().split())

a = float('inf')
for i in range(l, min(l + 2019, r + 1)):
    for j in range(i + 1, min(l + 2019, r + 1)):
        
        a = min(a, i * j % 2019)

print(a)
