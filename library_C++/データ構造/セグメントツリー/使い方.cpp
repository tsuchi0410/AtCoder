// セグ木の準備 (型: int, 演算方法: op, 単位元: e)
const int iINF = 1<<30;
vector<int> v(N);
SegmentTree<int> seg(v, [&](int a, int b){ return op; }, e);

// set O(log N)
seg.set(i, x);

// get [l, r), l and r are 0-indexed, O(log N)
seg.prod(l, r);

// all_get
seg.all_prod();

// get max r that f(get(l, r)) = True (0-indexed), O(log N)
int max_right(const function<bool(Monoid)> f, int l = 0);

// get min l that f(get(l, r)) = True (0-indexed), O(log N)
int min_left(const function<bool(Monoid)> f, int r = -1)


// セグ木上の二分探索の例
// x = seg.prod(L, r) として、f(x) = True となる最大の r を求める
// 例えば VAL = 3 とすると、3 以上がでてくる最大の index 返す
// 変更する所は VAL と L (左端のスタート地点)
int res = seg.max_right([&](int x) -> bool { return VAL > x; }, L);