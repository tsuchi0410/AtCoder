K = int(input())
# K = list(map(int,input().split()))

if K >= 60:
    print("22:"+str(f'{(K-60):02}'))
else:
    print("21:"+ str(f'{(K):02}'))

