# 二次元リストの転置
d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
t = [x for x in zip(*d)]
t = [list(_) for _ in t]