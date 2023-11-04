from math import factorial


def main():
    n = 10 ** 6  # n=100万
    n = n - 1  # 処理が0 = 1番目、1 = 2番目とn-1=n番目に対応しているので1を引く
    num_list = list(range(10))  # [0,1,2,3,4,5,6,7,8,9]を作成
    factorical_list = [factorial(i) for i in range(len(num_list))]  # 階乗のリストを作成 factorical_list = [0,1!,2!,3!,4!,5!,6!,7!,8!,9!]
    ans = '' #答え用の変数
    for f in reversed(factorical_list):  # 階乗のリストを逆順にfへ代入
        ans += str(num_list.pop(n // f))  # nをfで割った商のindexにある数字をansの後ろに付け加える
        n = n % f  # n/fの余りを新たなnとする
    print(ans)


if __name__ == '__main__':
    from time import time as t
    st = t()
    main()
    print(t() - st, 'sec')