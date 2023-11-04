print(bin(255))                 # 10進数 -> 2進数
print(hex(255))                 # 10進数 -> 16進数
print(num[2:])

print(int('0b11111111', 2))     # 2進数 -> 10進数
print(int('0xff', 16))          # 16進数 -> 10進数

# n 進数を 10 進数に変換
# ex) 8 進数 -> 10 進数
# 347 (8進法) = 3 × 8^2 + 4 × 8^1 + 7 × 8^0 = 231 (10進法)

# 10 進数を M 進数に変換
def f(N, M):
    L = []
    while True:
        x = N % M
        L.append(x)
        N //= M
        if N < M:
            L.append(N)
            break
    L.reverse()
    return L