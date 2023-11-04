N = int(input())
dic = {}
dic2 = {}
for i in range(N):
    S, T = map(str, input().split())
    T = int(T)
    if S in dic:
        pass
    else:
        dic[S] = T
        dic2[(S, T)] = i + 1

ans = []

num_max = -1
for k, v in dic.items():
    num_max = max(num_max, v)

for k, v in dic.items():
    if v == num_max:
        ans.append((k, v))

cnt = 10**18
for i in ans:
    cnt = min(cnt, dic2[i])

print(cnt)