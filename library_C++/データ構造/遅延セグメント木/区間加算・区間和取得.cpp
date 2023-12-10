using pll = pair<long long, long long>;
vector<pll> v(N, pll(0, 1));
const pll identity_monoid = {0, 0};  // {val, range}
const long long identity_action = 0;
auto op = [&](pll x, pll y) { return pll(x.first + y.first, x.second + y.second); };
auto mapping = [&](long long f, pll x) { return pll(x.first + f * x.second, x.second); };
auto composition = [&](long long g, long long f) { return g + f; };
LazySegmentTree<pll, long long> seg(v, op, mapping, composition, identity_monoid, identity_action);

seg.apply(l, r + 1, x);
seg.prod(l, r + 1).first