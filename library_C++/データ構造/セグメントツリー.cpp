"""
op, 単位元
最小値 : min(a, b), INF
最大値 : max(a, b), -INF
区間和 : a + b, 0
区間積 : a * n, 1
最大公約数 : math.gcd(a, b), 0
区間XOR : a ^ b, 0
"""

ll op(ll a, ll b) { return min(a, b); }
ll e() { return INF; }
ll jud;
bool f(ll x) { return x > jud; }

int main(){
    // 配列を初期化
    vl a(N);
    segtree<ll, op, e> seg(a);

    // get
    seg.get(i);
    // すべての値を確認
    rep(i, N) cout << seg.get(i) << " ";
    cout << endl;

    // set
    seg.set(i, x);

    // prod
    // [l, r) を探索
    seg.prod(l, r);

    // all_prod = prod(0, N)
    seg.all_prod();

    // セグメント上の二分探索
    // この例なら、配列の値 x が T 以上となる切れ目を探す
    // 始点は 0
    jud = T;
    ll idx = seg.max_right(0, f);

    
}