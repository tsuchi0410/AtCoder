n = int(input())

res = ""
while n > 0:
    if n % 2 == 0:
        n = n // 2
        res = "B" + res
    else:
        n -= 1
        res = "A" + res

print(res)