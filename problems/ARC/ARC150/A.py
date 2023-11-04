T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    S = list(input())
    ans = 0

    lst = [0]
    for i in range(N):
        if S[i] == "1":
            lst.append(lst[i] + 1)
        else:
            lst.append(lst[i])
    
    cnt = 0
    for i in range(K):
        if S[i] == "1" or S[i] == "?":
            cnt += 1
    
    if cnt == K and lst[K] == lst[-1]:
        ans += 1
    
    l = 0
    for r in range(K, N, 1):
        if S[r] == "1" or S[r] == "?":
            cnt += 1
        if S[l] == "1" or S[l] == "?":
            cnt -= 1
        l += 1
        if cnt == K and lst[0] == lst[l] and lst[r + 1] == lst[-1]:
            ans += 1

    if ans == 1:
        print("Yes")
    else:
        print("No")