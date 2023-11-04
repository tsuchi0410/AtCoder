M = int(input())
D = list(map(int, input().split()))

cnt = sum(D) // 2
for i in range(M):
    if cnt >= D[i]:
        cnt -= D[i]
    else:
        print(i + 1, cnt + 1)
        exit()