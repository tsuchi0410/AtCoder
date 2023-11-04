n = int(input())
s = input()

for i in range(1, n):
    cnt = 0
    for j in range(0, n, 1):
        if j+i >= n:
            break
        if s[j] == s[j+i]:
            break
        else:
            cnt += 1
    print(cnt)