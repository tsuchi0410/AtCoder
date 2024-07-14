"""
数値
"""
# 1 行 1 数値
N = int(input())

# 1 行 n 数値
A, B, C = map(int, input().split())

# 1 行 n 数値 -> リストに格納
L = list(map(int, input().split()))

# n 行 n 数値
N = int(input())
L = [int(input()) for _ in range(N)]

# n 行 n 数値 -> リストに格納
N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]


"""
文字列
"""
# 1 行 1 文字列
S = input()

# 1 行 n 文字列
A, B, C = input().split()

# 1 行 n 文字列 -> リストに格納
L = list(input().split())

# n 行 n 文字列
N = int(input())
L = [input() for _ in range(N)]

# n 行 n 文字列 -> リストに格納
N = int(input())
L = [list(input().split()) for _ in range(N)]


