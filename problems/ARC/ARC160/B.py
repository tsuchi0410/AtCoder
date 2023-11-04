T = int(input())
for _ in range(T):
    N = int(input())
    for x in range(1, int(N**0.5)+1):
        for y in range(1, int(N**0.5)+1):
            ans = x+y