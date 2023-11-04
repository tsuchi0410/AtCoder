from collections import defaultdict
N, Q = map(int, input().split())
A = list(map(int, input().split()))
dic = defaultdict(list)
for i in range(N):
    dic[A[i]].append(i)
for _ in range(Q):
    x, k = map(int, input().split())
    k -= 1
    if x in dic:
        if k < len(dic[x]):
            print(dic[x][k] + 1)
        else:
            print(-1)
    else:
        print(-1)