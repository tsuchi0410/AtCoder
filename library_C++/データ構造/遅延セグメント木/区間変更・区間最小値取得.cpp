const long long identity_monoid = (1LL << 31) - 1;
const long long identity_action = -1;
auto op = [&](long long x, long long y) { return min(x, y); };
auto mapping = [&](long long f, long long x) { return (f != identity_action ? f : x); };
auto composition = [&](long long g, long long f) { return (g != identity_action ? g : f); };
LazySegmentTree<long long, long long> seg(N, op, mapping, composition, identity_monoid, identity_action);

seg.set(i, x);
seg.apply(l, r + 1, x);
seg.prod(l, r + 1);