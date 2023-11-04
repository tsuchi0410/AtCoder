N = int(input())
a = list(map(int,input().split()))

cnt = {}
for i in range(max(a)+2):
    cnt[i] = 0

for i in a:
    cnt[i] += 1
    cnt[i+1] += 1
    if i != 0:
        cnt[i-1] += 1

print(max(cnt.values()))