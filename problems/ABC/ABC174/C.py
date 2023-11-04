k = int(input())

for i in range(k + 1):
    if i == 0:
        num = 7 % k
    else:
        num = (num * 10 + 7) % k

    if num == 0:
        print(i + 1)
        exit()

print(-1)