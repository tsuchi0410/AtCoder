import bisect
N = int(input())

res = ''
while N > 0:    
    if N % 2 == 0:
        N = N // 2
        res = 'B' + res
    else:
        N = N - 1
        res = 'A' + res

print(res)
