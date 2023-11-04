N = int(input())

ST = []
for i in range(N):
    S,T = (str(x) for x in input().split())
    ST.append([S,int(T)])

ST = sorted(ST, reverse=True, key=lambda x: x[1])
print(ST[1][0])

