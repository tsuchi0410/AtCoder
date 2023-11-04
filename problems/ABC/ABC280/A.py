h,w = (int(x) for x in input().split())
ans = 0
for i in range(h):
    s = input()
    ans += s.count('#')

print(ans)