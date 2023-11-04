N, K = map(int, input().split())
if int(str(K)[::-1]) < K:
    print(0)
    exit()
cnt = set()
num = K
while num <= N:
    if not num in cnt:
        cnt.add(num)
    num *= 10
num = str(K)
num = num[::-1]
num = int(num)
while num <= N:
    if not num in cnt:
        cnt.add(num)
    num *= 10
print(len(cnt))
