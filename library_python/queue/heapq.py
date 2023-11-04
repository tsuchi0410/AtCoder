import heapq

# 最小値取り出しの場合
A = [3,-1,4,-1,5,-9,26]

heapq.heapify(A)                # Aを優先度付きキューに変換する
heapq.heappush(A,-53)           # Aに値を挿入する
A_min = heapq.heappop(A)        # Aの最小値を取り出す   A_min = -53
print(A[0])                     # Aの最小値を参照する   -9


# 最大値取り出しの場合：-1倍して入れて、出すときに-1倍する
A = [3,-1,4,-1,5,-9,26]

B = [-A[i] for i in range(len(A))]              # 最小値取り出しのために-1倍しておく

heapq.heapify(B)                                # 優先度付きキューに変換する
heapq.heappush(B,-1 * -53)                      # 値(-53)を挿入する
A_max = -1 * heapq.heappop(B)                   # 最大値を取り出す      A_max = 26
print(-1 * B[0])                                # 最大値を参照する 5