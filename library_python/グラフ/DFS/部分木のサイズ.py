"""
部分木のサイズを求める
根から葉に向かって辺を貼る
"""

import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10 ** 8)

N = int(input())
G = [[] for _ in range(N)]
for i in range(N):
    u, v = map(int, input().split())
    G[u].append(v)

dp = [0] * N
def dfs(v):
    ans = 1
    for nv in G[v]:
        ans += dfs(nv)
    dp[v] = ans
    return ans
dfs(0)
print(*dp, sep="\n")