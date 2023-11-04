L, N1, N2 = map(int, input().split())
eveA = []
for i in range(N1):
    v, l = map(int, input().split())
    eveA.append([v, l])

eveB = []
for i in range(N2):
    v, l = map(int, input().split())
    eveB.append([v, l])

cntA = 0
cntB = 0
ans = 0
pre_num = 0
idxB = 0
f = False
for numA, lengthA in eveA:
    
    if f == False:
        pre_num = numA
        cntA += lengthA
        f = True
    elif pre_num == numA:
        cntA += lengthA
        if cntA < cntB:
            ans += lengthA
        else:
            ans += cntB - (cntA - lengthA)
        
    elif pre_num != numA:
        cntA += lengthA
    
    if cntB < cntA:
        pre_num = numA
        while cntB < cntA:
            cntB += eveB[idxB][1]
            numB = eveB[idxB][0]
            if pre_num == numB:
                if cntB < cntA:
                    ans += eveB[idxB][1]
                else:
                    ans += cntA - (cntB - eveB[idxB][1])
            idxB += 1
        pre_num = numB

print(ans)