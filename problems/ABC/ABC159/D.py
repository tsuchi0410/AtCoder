from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)
for i in range(N):
    d[A[i]] += 1

ans = 0
for k, v in d.items():
    ans += v * (v-1) // 2

for i in range(N):
    v = d[A[i]]
    num = ans - (v * (v-1) // 2)
    v -= 1
    print(num + v * (v-1) // 2)