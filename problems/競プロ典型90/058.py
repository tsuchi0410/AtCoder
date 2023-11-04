n, k = (int(x) for x in input().split())
MOD = 10 ** 5

cnt = 0
d = {}
d[n] = cnt
x = n
while True:
    y = 0
    xs = str(x)
    for i in range(len(xs)):
        y += int(xs[i])
    x = (x + y) % MOD
    cnt += 1
    
    if cnt == k:
        print(x)
        exit()
    elif x in d:
        c = cnt - d[x]
        k -= cnt
        k %= c
        k += d[x]
        for i in d:
            if d[i] == k:
                print(i)
                exit()
    else:
        d[x] = cnt
