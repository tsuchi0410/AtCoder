# 二次元リストを縦に回しながらループする
c = [input() for _ in range(n)]
for col in zip(*c):