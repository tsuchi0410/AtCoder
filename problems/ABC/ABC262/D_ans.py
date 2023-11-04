from typing import List


def main():
    # 入力受け取り
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    mod: int = 998244353

    answer: int = 0
    # 1以上N以下の整数lについてそれぞれ動的計画法で解を求める
    for l in range(1, N + 1):
        # DPテーブル
        # 内側の次元のリストの長さを制限しないとTLEするので注意
        dp: List[List[List[int]]] = [
            [[0 for k in range(l)] for j in range(l + 1)] for i in range(N + 1)
        ]

        # 初期条件
        for i in range(N + 1):
            dp[i][0][0] = 1

        # 遷移
        for i in range(1, N + 1):
            for j in range(1, l + 1):
                for k in range(l):
                    # i番目の要素を選ばない場合
                    dp[i][j][k] += dp[i - 1][j][k]

                    # i番目の要素を選ぶ場合
                    dp[i][j][k] += dp[i - 1][j - 1][(k - (A[i - 1] % l)) % l]

                    # 余りを取る
                    dp[i][j][k] %= mod

            for m in dp:
                print(m)
            print()

        # 解を足し合わせる
        answer += dp[N][l][0] % mod

    print(answer % mod)


if __name__ == "__main__":
    main()
