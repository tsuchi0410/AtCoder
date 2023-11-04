import math
import numpy as np
t = int(input())
l,x,y = (int(x) for x in input().split())
Q = int(input())
pi = math.pi
for i in range(Q):
    q = int(input())
    theta = (q/t) * (2*pi)
    n1 = -l/2 * math.sin(pi/2-theta)
    n2 = l/2 - l/2 * math.sin(pi/2-theta)

    # 点A,B,Cの座標（3次元座標上の場合）
    a = np.array([0,n1,n2])
    b = np.array([0,n1,0])
    c = np.array([x,y,0])
    print(a)
    print(b)
    print(c)
    # ベクトルを定義
    vec_a = a - b
    vec_c = c - b

    # コサインの計算
    length_vec_a = np.linalg.norm(vec_a)
    length_vec_c = np.linalg.norm(vec_c)
    inner_product = np.inner(vec_a, vec_c)
    cos = inner_product / (length_vec_a * length_vec_c)

    # 角度（ラジアン）の計算
    rad = np.arccos(cos)

    # 弧度法から度数法（rad ➔ 度）への変換
    degree = np.rad2deg(rad)
    print(degree)