N = int(input())
N -= 1
ans = []
while True:
    num = N % 26
    ans.append(chr(num + 97))
    if N >= 26:
        N = N // 26 - 1
    else:
        break
ans.reverse()
print("".join(ans))