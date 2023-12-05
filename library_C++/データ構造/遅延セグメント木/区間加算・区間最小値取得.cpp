vector<long long> v(N, 0);
const long long identity_monoid = (1LL << 31) - 1;
const long long identity_action = 0;
auto op = [&](long long x, long long y) { return min(x, y); };
auto mapping = [&](long long f, long long x) { return f + x; };
auto composition = [&](long long g, long long f) { return g + f; };
LazySegmentTree<long long, long long> seg(v, op, mapping, composition, identity_monoid, identity_action);

seg.apply(l, r + 1, x);
seg.prod(l, r + 1);