A, B, W = (int(x) for x in input().split())

W = 1000 * W
x = float('inf')
y = float('inf') * -1
for n in range(1, 10 ** 6 + 1):
    l = n * A
    r = n * B
    if l <= W <= r:
        x = min(x, n)
        y = max(y, n)

if x == float('inf') or y == float('inf') * -1:
    print('UNSATISFIABLE')
else:
    print(x, y)
    