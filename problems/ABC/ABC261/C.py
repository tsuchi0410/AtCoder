N = int(input())
#L = list(map(int,input().split()))
#X, Y, Z = (int(x) for x in input().split())

S = []
Sdic = {}
maxSdic= {}
for i in range(N):
    ip = str(input())
    S.append(ip)

    if ip in Sdic.keys():
        Sdic[ip] += 1
        maxSdic[ip] += 1
    else:
        Sdic[ip] = 0
        maxSdic[ip] = 0

# count

for i in range(N):
    if abs((Sdic[S[i]]) - (maxSdic[S[i]])) == 0:
        print(S[i])
        Sdic[S[i]] -= 1
    
    else:
        buf = "(" + str(abs((Sdic[S[i]]) - (maxSdic[S[i]]))) + ")"
        print(S[i]+buf)
        Sdic[S[i]] -= 1
    
