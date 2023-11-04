N,K = (int(x) for x in input().split())

for _ in range(K):
    if N % 200 == 0:
        N = int(N / 200)
    else:
        N = str(N)
        N = N + "200"
        N = int(N)

print(N)