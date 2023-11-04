# スタックオーバーフローを防ぐ
import sys
sys.setrecursionlimit(10 ** 6)

# 頂点数
N = int(input())
# 親頂点
P = list(map(int,input().split()))

# 頂点ｖを根とする部分木を探索
def rec(v, chs):
    print(v, end = ' ')
    
    # 再帰的に探索
    for ch in chs[v]:
        rec(ch, chs)

# 各頂点の子頂点リストを作成
chs = [[] for _ in range(N)]
for i in range(N-1):
    chs[P[i]].append(i+1)
    
# print(chs)

# 根頂点０から再帰的に探索
rec(0, chs)