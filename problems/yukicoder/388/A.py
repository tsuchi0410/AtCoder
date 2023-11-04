N = int(input())
ans = 0
if N % 3 == 0:
    ans = 0
elif N % 3 == 1:
    ans = 2
elif N % 3 == 2:
    ans = 1
print(ans)