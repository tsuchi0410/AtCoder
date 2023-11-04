import bisect

N,P,Q,R = (int(x) for x in input().split())
A = list(map(int,input().split()))

sumlist = [0]
for i in range(0, N):
    sumlist.append(sumlist[i]+A[i])

# print(sumlist)

# xを固定
for i in range(0, N):

    Sy_idx = bisect.bisect_left(sumlist, P + sumlist[i])
    
    if Sy_idx >= len(sumlist) or sumlist[Sy_idx] != P + sumlist[i]:
        continue
    
    Sz_idx = bisect.bisect_left(sumlist, Q + sumlist[Sy_idx])
        
    if Sz_idx >= len(sumlist) or sumlist[Sz_idx] != Q + sumlist[Sy_idx]:
        continue
    
    Sw_idx = bisect.bisect_left(sumlist, R + sumlist[Sz_idx])
            
    if Sw_idx >= len(sumlist) or sumlist[Sw_idx] != R + sumlist[Sz_idx]:
        continue
    
    print('Yes')
    exit()

print('No')        