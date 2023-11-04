from collections import deque

q = deque()
for right in S:
    
    q.append(right) # 右端を追加
    # 追加した要素に応じた処理

    # while q and (満たすべき条件):
    while q: 
        
        left = q.popleft() # 条件を満たさないとき左端を取り除く
        # 取り除いた要素に応じた処理
    # 連続部分列を満たしているときの処理
