from collections import defaultdict
N = int(input())
dic = defaultdict(int)
for i in range(N):
    s = input()
    s = tuple(sorted(s))
    dic[s] += 1
ans = 0
for key, val in dic.items():
    ans += val * (val - 1) // 2
print(ans)
