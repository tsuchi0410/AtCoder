import itertools
N,M= (int(x) for x in input().split())

l = list(itertools.combinations(range(1,M+1), N))
l2 = []
for i in l:
    print(" ".join(map(str,i)))