L = list(map(int,input().split()))
print(max(min(L[1],L[3]) - max(L[0],L[2]), 0))
