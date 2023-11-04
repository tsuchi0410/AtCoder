"""
ステップ1: 加算処理
・区間 [l, r] に v を加算したいとき、l 番目の値に v を加算する
・r + 1 番目の値に -v を加算する
ステップ2: 累積和
・最後に累積和をすると、最終結果を得られる
"""

D = int(input())
N = int(input())
imos = [0] * (D + 1)
for i in range(N):
    L, R = map(int, input().split())
    
    # 区間の調整
    # L -= 1
    # 区間にvを加算
    imos[L] += 1
    imos[R] -= 1

# 累積和
S = [0]
for i in range(D + 1):
    S.append(S[i] + imos[i])

print(*S[1:(D + 1)], sep = "\n")