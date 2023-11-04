import random
import math
from collections import defaultdict

# 段数
N = 30
# ベクトル
VEC = [[-1, -1], [-1, 0], [0, -1], [0, 1], [1, 0], [1, 1]]
LOOP = 5 * 10**5

START_TEMP = 100
END_TEMP = 10
TEMP = []
for i in range(LOOP):
    TEMP.append(START_TEMP / math.log(i + 2, 2))

def main():
    # read
    ball = []
    dic = {}
    for i in range(N):
        b = list(map(int, input().split()))
        ball.append(b)
        for j in range(len(b)):
            dic[b[j]] = [i, j]
    
    # 探索開始
    ans = []
    for i in range(LOOP):
        if len(ans) == 10000:
            break
        # ランダムに ball を 1 個選ぶ
        now_ball = random.randint(0, 464)
        now_y = dic[now_ball][0]
        now_x = dic[now_ball][1]

        # スコア計算
        now_E = calculate_score(ball, now_y, now_x)

        # 6 方向に動かしてスコアがよくなる方向にボールを交換
        new_E = 0
        delta = -10 ** 18
        for y, x in VEC:
            target_y = now_y + y
            target_x = now_x + x
            
            if not 0 <= target_y < N:
                continue
            if not 0 <= target_x < len(ball[target_y]):
                continue
            
            # swap
            ball[now_y][now_x], ball[target_y][target_x] = ball[target_y][target_x], ball[now_y][now_x]
            new_E = calculate_score(ball, now_y, now_x)
            
            if delta < now_E - new_E:
                yy = target_y
                xx = target_x
                delta = now_E - new_E
            
            ball[now_y][now_x], ball[target_y][target_x] = ball[target_y][target_x], ball[now_y][now_x]
 
        # 温度関数
        T = TEMP[i]

        # 遷移
        cal = delta / T

        if cal > 0:
            P = -math.log(cal, 10)
        else:
            P = 0.02

        # 入れ替え
        while True:
            rand = random.uniform(0, 1)
            if 0 < rand < 1:
                break
        if rand < P:
            ball[now_y][now_x], ball[yy][xx] = ball[yy][xx], ball[now_y][now_x]
            ans.append([now_y, now_x, yy, xx])  
            continue

    print(len(ans))
    for y1, x1, y2, x2 in ans:
        print(y1, x1, y2, x2)


def calculate_score(ball, y, x):
    E = 0
    # 下(1組)
    if 0 <= y < N - 1:
        a = ball[y][x]
        b = ball[y + 1][x]
        c = ball[y + 1][x + 1]
        if a > b or a > c:
            E += 1
    # 上(2組)
    if 1 <= y < N and 1 <= x:
        a = ball[y - 1][x - 1]
        c = ball[y][x]
        if a > c:
            E += 1
    if 1 <= y < N and x < len(ball[y]) - 1:
        a = ball[y - 1][x]
        b = ball[y][x]
        if a > b:
            E += 1

    return E

if __name__ == "__main__":
    main()