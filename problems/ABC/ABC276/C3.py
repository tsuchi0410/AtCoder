from math import factorial

def main():
    import sys
    input = sys.stdin.readline
 
    class Bit:
        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)
 
        def sum(self, i):
            s = 0
            while i > 0:
                s += self.tree[i]
                i -= i & -i
            return s
 
        def add(self, i, x):
            while i <= self.size:
                self.tree[i] += x
                i += i & -i
 
        def lower_bound(self, w):
            if w <= 0:
                return 0
            x = 0
            k = 1 << (self.size.bit_length() - 1)
            while k:
                if x + k <= self.size and self.tree[x + k] < w:
                    w -= self.tree[x + k]
                    x += k
                k >>= 1
            return x + 1
 
    N = int(input())
    A = list(map(int, input().split()))
 
    fac = [1] * (N+1)
    for i in range(1, N+1):
        fac[i] = (fac[i-1] * i)
 
    bit = Bit(N)
    for i in range(1, N+1):
        bit.add(i, 1)
    ans = 1
    for i, a in enumerate(A):
        x = bit.sum(a) - 1
        ans = (ans + x * fac[N - 1 - i])
        bit.add(a, -1)
    
    n = ans-1
    n = n - 1  # 処理が0 = 1番目、1 = 2番目とn-1=n番目に対応しているので1を引く
    num_list = list(range(N+1))
    num_list = num_list[1:]

    factorical_list = [factorial(i) for i in range(len(num_list))]  # 階乗のリストを作成 factorical_list = [0,1!,2!,3!,4!,5!,6!,7!,8!,9!]
    ans = []
    for f in reversed(factorical_list):  # 階乗のリストを逆順にfへ代入
        ans.append(str(num_list.pop(n // f)))  # nをfで割った商のindexにある数字をansの後ろに付け加える
        n = n % f  # n/fの余りを新たなnとする
    print(*ans)
 
 
if __name__ == '__main__':
    main()