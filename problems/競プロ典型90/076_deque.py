from collections import deque
N = int(input())
A = list(map(int,input().split()))
ans = sum(A)
B = A[:]
L = A + B

cnt = 0
q = deque()
for right in L:
    
    q.append(right) # 右端を追加
    cnt += right
    # 追加した要素に応じた処理
    if cnt * 10 == ans:
        print("Yes")
        exit()

    # while q and (満たすべき条件):
    while cnt * 10 > ans or len(q) > N: 
        left = q.popleft() # 条件を満たさないとき左端を取り除く
        # 取り除いた要素に応じた処理
        cnt -= left

print("No")