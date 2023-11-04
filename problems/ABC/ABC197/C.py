N = int(input())
A = list(map(int, input().split()))

NUM = N
ans = float("inf")
for i in range(2 ** NUM):
    l = [i >> j & 1 for j in range(NUM)]
    cnt = []
    num = -1
    for j in range(len(l) - 1):
        if l[j] == l[j + 1]:
            if num == -1:
                num = A[j]
            else:
                num |= A[j]
        else:
            if num == -1:
                num = A[j]
            else:
                num |= A[j] 
            cnt.append(num)
            num = -1
    if num == -1:
        cnt.append(A[-1])
    else:
        num |= A[-1]
        cnt.append(num)
    
    if len(cnt) == 1:
        ans = min(ans, cnt[0])
    else:
        num = cnt[0]
        for j in range(1, len(cnt)):
            num ^= cnt[j]
        ans = min(ans, num)

print(ans)