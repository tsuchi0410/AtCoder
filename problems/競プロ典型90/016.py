n = int(input())
a, b, c = (int(x) for x in input().split())

ans = float('inf')
for i in range(0, 10000):
    for j in range(0, 10000):
        if n - (a * i + b * j) >= 0 and (n - (a * i + b * j)) % c == 0:
            ans = min(ans, i + j + ((n - (a * i + b * j)) // c))

print(ans)