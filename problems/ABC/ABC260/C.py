N, X, Y = (int(x) for x in input().split())

rj_count = 1
bj_count = 0

f = 0
while f == 0:
    if N >= 2:
        bj_count = bj_count + rj_count * X
        rj_count = rj_count + bj_count 
        bj_count = bj_count * Y
        N -= 1
    else:
        f = 1

print(bj_count)

        

        