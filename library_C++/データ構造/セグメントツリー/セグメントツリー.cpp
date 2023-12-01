// Segment Tree
template<class Monoid> struct SegmentTree {
  using Func = function<Monoid(Monoid, Monoid)>;

  // core member
  int N;
  Func OP;
  Monoid IDENTITY;
  
  // inner data
  int log, offset;
  vector<Monoid> dat;

  // constructor
  SegmentTree() {}
  SegmentTree(int n, const Func &op, const Monoid &identity) {
    init(n, op, identity);
  }
  SegmentTree(const vector<Monoid> &v, const Func &op, const Monoid &identity) {
    init(v, op, identity);
  }
  void init(int n, const Func &op, const Monoid &identity) {
    N = n;
    OP = op;
    IDENTITY = identity;
    log = 0, offset = 1;
    while (offset < N) ++log, offset <<= 1;
    dat.assign(offset * 2, IDENTITY);
  }
  void init(const vector<Monoid> &v, const Func &op, const Monoid &identity) {
    init((int)v.size(), op, identity);
    build(v);
  }
  void pull(int k) {
    dat[k] = OP(dat[k * 2], dat[k * 2 + 1]);
  }
  void build(const vector<Monoid> &v) {
    assert(N == (int)v.size());
    for (int i = 0; i < N; ++i) dat[i + offset] = v[i];
    for (int k = offset - 1; k > 0; --k) pull(k);
  }
  int size() const {
    return N;
  }
  Monoid operator [] (int i) const {
    return dat[i + offset];
  }
  
  // update A[i], i is 0-indexed, O(log N)
  void set(int i, const Monoid &v) {
    assert(0 <= i && i < N);
    int k = i + offset;
    dat[k] = v;
    while (k >>= 1) pull(k);
  }
  
  // get [l, r), l and r are 0-indexed, O(log N)
  Monoid prod(int l, int r) {
    assert(0 <= l && l <= r && r <= N);
    Monoid val_left = IDENTITY, val_right = IDENTITY;
    l += offset, r += offset;
    for (; l < r; l >>= 1, r >>= 1) {
      if (l & 1) val_left = OP(val_left, dat[l++]);
      if (r & 1) val_right = OP(dat[--r], val_right);
    }
    return OP(val_left, val_right);
  }
  Monoid all_prod() {
    return dat[1];
  }
  
  // get max r that f(get(l, r)) = True (0-indexed), O(log N)
  // f(IDENTITY) need to be True
  int max_right(const function<bool(Monoid)> f, int l = 0) {
    if (l == N) return N;
    l += offset;
    Monoid sum = IDENTITY;
    do {
      while (l % 2 == 0) l >>= 1;
      if (!f(OP(sum, dat[l]))) {
        while (l < offset) {
          l = l * 2;
          if (f(OP(sum, dat[l]))) {
            sum = OP(sum, dat[l]);
            ++l;
          }
        }
        return l - offset;
      }
      sum = OP(sum, dat[l]);
      ++l;
    } while ((l & -l) != l);  // stop if l = 2^e
    return N;
  }

  // get min l that f(get(l, r)) = True (0-indexed), O(log N)
  // f(IDENTITY) need to be True
  int min_left(const function<bool(Monoid)> f, int r = -1) {
    if (r == 0) return 0;
    if (r == -1) r = N;
    r += offset;
    Monoid sum = IDENTITY;
    do {
      --r;
      while (r > 1 && (r % 2)) r >>= 1;
      if (!f(OP(dat[r], sum))) {
        while (r < offset) {
          r = r * 2 + 1;
          if (f(OP(dat[r], sum))) {
            sum = OP(dat[r], sum);
            --r;
          }
        }
        return r + 1 - offset;
      }
      sum = OP(dat[r], sum);
    } while ((r & -r) != r);
    return 0;
  }
  
  // debug
  friend ostream& operator << (ostream &s, const SegmentTree &seg) {
    for (int i = 0; i < (int)seg.size(); ++i) {
      s << seg[i];
      if (i != (int)seg.size() - 1) s << " ";
    }
    return s;
  }
};