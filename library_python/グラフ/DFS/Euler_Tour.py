"""
オイラーツアー
木をDFSしたときの順番で頂点を記録する手法
"""

from collections import defaultdict, deque, Counter

def euler_tour(G, root):
    
    euler = []
    stack = deque([root])
    q = deque()
    seen = [False] * N # N:頂点数
    while stack:
        v = stack.pop()
        euler += [v]
        if seen[v]:
            continue
        for next_v in reversed(G[v]): # reversedで数の小さい方から見る
            # [親頂点、子頂点、子頂点、。。。]と入れていく.その後連結
            if seen[next_v]:
                stack += [next_v]
            else:
                q += [next_v]
        stack.extend(q)
        q = deque()
        seen[v] = True
    
    return euler

