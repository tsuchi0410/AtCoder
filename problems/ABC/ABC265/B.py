N,M,T = (int(x) for x in input().split())
A = list(map(int,input().split()))
B = {}
for i in range(M):
    aa,bb = (int(x) for x in input().split())
    B[aa] = bb

cnt = 1
for i in range(N-1):
    
    # 失敗
    if T <= A[i]:
        print("No")
        exit()

    # 移動
    T -= A[i]
    cnt += 1

    # 持ち時間増加
    if cnt in B:
        T += B[cnt]
    

print("Yes")
