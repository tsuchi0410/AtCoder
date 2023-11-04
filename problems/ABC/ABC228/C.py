N,K = (int(x) for x in input().split())
P=[]
for i in range(N):
    P.append(list(map(int,input().split())))

tensu=[]
for i in range(N):
    tensu.append([sum(P[i])*-1, i])

tensu = sorted(tensu)

#print(tensu)

ans = []
for i in range(N):
    
    if tensu[K-1][0] >= tensu[i][0]-300: 
        ans.append(["Yes",tensu[i][1]])
    else:
        ans.append(["No",tensu[i][1]])

#print(tensu)
#print(ans)

l = sorted(ans, key=lambda x: x[1])
#print(l)
for i in range(N):
    print(l[i][0])
