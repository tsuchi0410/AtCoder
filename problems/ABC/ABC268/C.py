from collections import defaultdict

N = int(input())
p = list(map(int,input().split()))


#cnt = 0
# for i in range(N):
#     if p[i-1] % N == i or p[i] == i or p[i+1] % N == i:
#         cnt += 1

l = []
d = defaultdict(int)
for i in range(N):
    l.append(p[i]-i)
        
for i in range(N):
    d[l[i]] += 1

a = float('inf')*-1
for i in d:
    a = max(a,d[i])

m = []
for i in d:
    if d[i] == a:
        m.append(i)

ans = 0
b = 0
for i in range(len(m)):
    cnt = 0
    for j in range(len(l)):
        b = l[j]-m[i]

        if (b-1) % N == 0 or b == 0 or (b+1)%N == 0:
            cnt += 1

    ans = max(ans,cnt)

print(m)
print(l)
print(ans)