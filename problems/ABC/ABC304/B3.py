N = int(input())
cnt = 0
for i in range(3, 10):
    if N < 10**i:
        N /= (10**cnt)
        N = int(N) * (10**cnt)
        break
    cnt += 1
print(N)