t = int(input())
for i in range(t):
    a, s = map(int, input().split())
    if a <= s:
        # a&(s-a)=a
        if a & (s-a) == a:
            print('Yes')
            continue
    print('No')
