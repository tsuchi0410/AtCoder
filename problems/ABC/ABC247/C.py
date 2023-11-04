n = int(input())

if n == 1:
    print(1)
else:
    ans = [1]
    for i in range(1, n):
        res = ans + [i+1] + ans
        ans = res
    for i in range(len(ans)):
        ans[i] = str(ans[i])

    print(' '.join(ans))