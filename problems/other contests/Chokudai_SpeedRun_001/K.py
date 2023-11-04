from math import factorial

def get_rank(target):
    nums = list(range(1000000))  # [0,1,2,3,4,5,6,7,8,9]を作成
    # 並べ替えた結果を格納するリスト
    result = []
    # 階乗を事前に計算
    factorials = [factorial(i) for i in range(len(target))]
    # インデックスを初期化
    index = 0
    # 順番に数字を決定していく
    for i in range(len(target), 0, -1):
        # 次にくる数字のインデックスを計算
        digit_index = nums.index(target[index])
        # その数字が来る場合のパターン数を計算
        pattern = digit_index * factorials[i-1]
        # 結果に追加
        result.append(pattern)
        # インデックスを更新
        index += 1
        # 決定した数字をリストから削除
        nums.pop(digit_index)
    # パターン数を合計して、1を足して返す
    return sum(result) + 1

N = int(input())
L = list(map(int, input().split()))

print(get_rank(L))