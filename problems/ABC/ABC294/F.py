"""
<=> 濃度 x が与えられる。 NM 通りの砂糖水のうち濃度が x 未満である砂糖水は何本あるか？

砂糖水 s グラム、水 t グラムの砂糖水を考える。
濃度 x の砂糖水の砂糖と水の比は x : 1 - x だから、 s : t = x : 1 - x
-> 砂糖の量が s = t * x / (1 - x) であれば丁度濃度が x となる

u = t * x / (1 - x) とすると、
・if s >= u 砂糖が s - u グラム余っている
・elif s <= u 砂糖が u - s グラム足りない

2 つの砂糖水を混ぜたとき、濃度が x 以上であるかは、
それぞれの砂糖水について s - u を足し合わせた値が 0 以上であるか見ればいい

"""
import bisect
N, M, K = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    
C = []
D = []
for i in range(M):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)

def is_ok(mid):
    # 条件を満たすかどうか？問題ごとに定義
    z = mid / (1 - mid)
    # v = s - u
    v = []
    for i in range(M):
        v.append(C[i] - D[i] * z)
    v.sort()
    y = 0
    print(v)
    for i in range(N):
        w = A[i] - B[i] * z
        # v + w >= mid
        idx = bisect.bisect_left(v, w)
        y += M - idx
    return y

def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    for _ in range(10**4):
        mid = (ok + ng) / 2
        if is_ok(mid) < K:
            ok = mid
        else:
            ng = mid
        print(mid)
    return ok

print(meguru_bisect(0, 1))