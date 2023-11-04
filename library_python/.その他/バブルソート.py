# cnt = バブルソートした回数
cnt = 0
while(1):
    f = 0
    for i in range(N):
        if L[i+1] < L[i]:
            L[i],L[i+1] = L[i+1],L[i]
            cnt += 1
            f = 1
            
    if f == 0:
        print(cnt)
        exit()

    