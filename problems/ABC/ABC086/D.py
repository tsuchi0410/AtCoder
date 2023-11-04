N, H = map(int,input().split())
L = []
top_a = 0
for i in range(N):
    a, b = map(int,input().split())
    L.append(b)
    top_a = max(top_a, a)

L.sort(reverse = True)
ans = 0
for bi in L:
    if bi >= top_a:
        H -= bi
        ans += 1
    if H <= 0:
        break

if H > 0:
    if H % top_a == 0:
        ans += H // top_a
    else:
        ans += H // top_a + 1

print(ans)