#include <bits/stdc++.h>
using namespace std;

/* 型, 定数 */
using ll = long long;
using ull = unsigned long long;
using i128 = __int128;
using ld = long double;
// cout << fixed << setprecision(10);
const ll INF = 1e18;
const ld PI = acos(-1);
const ll MOD = 998244353;
// const ll MOD = 1000000007;

/* 関数 */
#define ctoll(x) static_cast<long long>(x - '0')
#define lltos(x) to_string(x)
#define lltoc(x) static_cast<char>(x + '0')
#define all(v) (v).begin(),(v).end()
#define len(v) ll(v.size())
template<class T> auto min(const vector<T>& a){ return *min_element(all(a)); }
template<class T> auto min(const set<T>& s){ return *(s.begin()); }
template<class T, class U> auto min(const map<T, U>& mp){ return *(mp.begin()); }
template<class T> auto max(const T& a){ return *max_element(all(a)); }
template<class T> auto max(const set<T>& s){ return *(--s.end()); }
template<class T, class U> auto max(const map<T, U>& mp){ return *(--mp.end()); }
template<class T, class U>ll count(const T& a, const U& b){ return count(all(a), b); }
template <typename T>
long long index(const T& ctr, const T& subctr) {
  auto itr = search(ctr.begin(), ctr.end(), subctr.begin(), subctr.end());
  if(itr == ctr.end()){
    return -1;
  }else{
    return distance(ctr.begin(), itr);
  }
}
template<typename T>
auto sum(vector<T>& v){
  return accumulate(v.begin(), v.end(), 0LL);
}
template <typename T>
vector<T> cum(vector<T> &v){
  vector<T> s = {0};
  for(ll i = 0; i < (ll)v.size(); i++) s.push_back(s[i] + v[i]);
  return s;
}
ll powll(ll n, ll r){
  if (r == 0) return 1;
  else if (r % 2 == 0) return powll(n * n, (ll)(r / 2));
  else return n * powll(n, r - 1);
}
template <typename T>
unordered_map<T, ll> ucounter(vector<T> &v){
  unordered_map<T, ll> mp;
  for(ll i = 0; i < (ll)v.size(); i++) mp[v[i]]++;
  return mp;
}
unordered_map<char, ll> ucounter(string &v){
  unordered_map<char, ll> mp;
  for(ll i = 0; i < (ll)v.size(); i++) mp[v[i]]++;
  return mp;
}
template <typename T>
map<T, ll> counter(vector<T> &v){
  map<T, ll> mp;
  for(ll i = 0; i < (ll)v.size(); i++) mp[v[i]]++;
  return mp;
}
map<char, ll> counter(string &v){
  map<char, ll> mp;
  for(ll i = 0; i < (ll)v.size(); i++) mp[v[i]]++;
  return mp;
}
#define unique(v) sort(all(v)), v.erase(unique(all(v)), v.end()), v.shrink_to_fit()
template<class T> 
auto reverse(T& x){ return reverse(x.begin(), x.end()); }
template<typename T> void chmin(T& a, T b) { a = min(a, b); }
template<typename T> void chmax(T& a, T b) { a = max(a, b); }
template <typename T> ll bisect_left(vector<T> &X, ll v){ return lower_bound(X.begin(), X.end(), (ll)v) - X.begin(); }
template <typename T> ll bisect_right(vector<T> &X, ll v){ return upper_bound(X.begin(), X.end(), (ll)v) - X.begin(); }

/* ソート */
template<class T> 
auto sort(vector<T>& v){ return stable_sort(v.begin(), v.end()); }
template<class T, class U>
auto sort(vector<T>& v, U idx){
  return stable_sort(v.begin(), v.end(), [&](const vector<long long> &_a_, const vector<long long> &_b_){return _a_[idx] < _b_[idx];});
}
template<class T> 
auto rsort(vector<T>& v){ return stable_sort(v.rbegin(), v.rend()); }
template<class T, class U>
auto rsort(vector<T>& v, U idx){
  return stable_sort(v.rbegin(), v.rend(), [&](const vector<long long> &_a_, const vector<long long> &_b_){return _a_[idx] < _b_[idx];});
}

/* ループ */
#define OVERLOAD_REP(_1, _2, _3, _4, name, ...) name
#define REP1(i, n) for (ll i = (ll)0; i != (ll)n; ++i)
#define REP2(i, l, r) for (ll i = (ll)l; i != (ll)r; ++i)
#define REP3(i, l, r, s) for (ll i = (ll)l; i < (ll)r; i += (s))
#define rep(...) OVERLOAD_REP(__VA_ARGS__, REP3, REP2, REP1)(__VA_ARGS__)
#define OVERLOAD_RREP(_1, _2, _3, _4, name, ...) name
#define RREP1(i, n) for (ll i = (ll)n; i != (ll)-1; --i)
#define RREP2(i, l, r) for (ll i = (ll)l; i != (ll)r; --i)
#define RREP3(i, l, r, s) for (ll i = (ll)l; i > (ll)r; i -= (s))
#define rrep(...) OVERLOAD_RREP(__VA_ARGS__, RREP3, RREP2, RREP1)(__VA_ARGS__)
#define OVERLOAD_FORE(_1, _2, _3, name, ...) name
#define FORE1(i, a) for(auto &i : a)
#define FORE2(i, j, a) for(auto &[i, j] : a)
#define fore(...) OVERLOAD_FORE(__VA_ARGS__, FORE2, FORE1)(__VA_ARGS__)

/* コンテナ */
#define discard(s, x) {auto itr_ = s.find((x)); if (itr_ != s.end()) s.erase(itr_); }
template <class T>
using pq = priority_queue<T>;  // 大きい順に取り出す
template <class T>
using pqg = priority_queue<T, vector<T>, greater<T>>;  // 小さい順に取り出す
// unordered_set, unordered_multiset, unordered_map, unordered_multimap で pair, vector, tuple を key に設定させる
template<class T> size_t HashCombine(const size_t seed,const T &v){
  return seed^(std::hash<T>()(v)+0x9e3779b9+(seed<<6)+(seed>>2));
}
template<class T,class S> struct std::hash<std::pair<T,S>>{
  size_t operator()(const std::pair<T,S> &keyval) const noexcept {
    return HashCombine(std::hash<T>()(keyval.first), keyval.second);
  }
};
template<class T> struct std::hash<std::vector<T>>{
  size_t operator()(const std::vector<T> &keyval) const noexcept {
    size_t s=0;
    for (auto&& v: keyval) s=HashCombine(s,v);
    return s;
  }
};
template<int N> struct HashTupleCore{
  template<class Tuple> size_t operator()(const Tuple &keyval) const noexcept{
    size_t s=HashTupleCore<N-1>()(keyval);
    return HashCombine(s,std::get<N-1>(keyval));
  }
};
template <> struct HashTupleCore<0>{
  template<class Tuple> size_t operator()(const Tuple &keyval) const noexcept{ return 0; }
};
template<class... Args> struct std::hash<std::tuple<Args...>>{
  size_t operator()(const tuple<Args...> &keyval) const noexcept {
    return HashTupleCore<tuple_size<tuple<Args...>>::value>()(keyval);
  }
};

// modint
// https://github.com/drken1215/algorithm/blob/master/MathNumberTheory/modint.cpp
template<int MOD> struct Fp {
  // inner value
  long long val;
  
  // constructor
  constexpr Fp() : val(0) { }
  constexpr Fp(long long v) : val(v % MOD) {
    if (val < 0) val += MOD;
  }
  
  // getter
  constexpr long long get() const {
    return val;
  }
  constexpr int get_mod() const {
    return MOD;
  }
  
  // comparison operators
  constexpr bool operator == (const Fp &r) const {
    return this->val == r.val;
  }
  constexpr bool operator != (const Fp &r) const {
    return this->val != r.val;
  }
  
  // arithmetic operators
  constexpr Fp& operator += (const Fp &r) {
    val += r.val;
    if (val >= MOD) val -= MOD;
    return *this;
  }
  constexpr Fp& operator -= (const Fp &r) {
    val -= r.val;
    if (val < 0) val += MOD;
    return *this;
  }
  constexpr Fp& operator *= (const Fp &r) {
    val = val * r.val % MOD;
    return *this;
  }
  constexpr Fp& operator /= (const Fp &r) {
    long long a = r.val, b = MOD, u = 1, v = 0;
    while (b) {
      long long t = a / b;
      a -= t * b, swap(a, b);
      u -= t * v, swap(u, v);
    }
    val = val * u % MOD;
    if (val < 0) val += MOD;
    return *this;
  }
  constexpr Fp operator + () const { return Fp(*this); }
  constexpr Fp operator - () const { return Fp(0) - Fp(*this); }
  constexpr Fp operator + (const Fp &r) const { return Fp(*this) += r; }
  constexpr Fp operator - (const Fp &r) const { return Fp(*this) -= r; }
  constexpr Fp operator * (const Fp &r) const { return Fp(*this) *= r; }
  constexpr Fp operator / (const Fp &r) const { return Fp(*this) /= r; }
  
  // other operators
  constexpr Fp& operator ++ () {
    ++val;
    if (val >= MOD) val -= MOD;
    return *this;
  }
  constexpr Fp& operator -- () {
    if (val == 0) val += MOD;
    --val;
    return *this;
  }
  constexpr Fp operator ++ (int) {
    Fp res = *this;
    ++*this;
    return res;
  }
  constexpr Fp operator -- (int) {
    Fp res = *this;
    --*this;
    return res;
  }
  friend constexpr istream& operator >> (istream &is, Fp<MOD> &x) {
    is >> x.val;
    x.val %= MOD;
    if (x.val < 0) x.val += MOD;
    return is;
  }
  friend constexpr ostream& operator << (ostream &os, const Fp<MOD> &x) {
    return os << x.val;
  }
  
  // other functions
  constexpr Fp pow(long long n) const {
    Fp res(1), mul(*this);
    while (n > 0) {
      if (n & 1) res *= mul;
      mul *= mul;
      n >>= 1;
    }
    return res;
  }
  constexpr Fp inv() const {
    Fp res(1), div(*this);
    return res / div;
  }
  friend constexpr Fp<MOD> pow(const Fp<MOD> &r, long long n) {
    return r.pow(n);
  }
  friend constexpr Fp<MOD> inv(const Fp<MOD> &r) {
    return r.inv();
  }
};

// Binomial coefficient
template<class mint> struct BiCoef {
  vector<mint> fact_, inv_, finv_;
  constexpr BiCoef() {}
  constexpr BiCoef(int n) : fact_(n, 1), inv_(n, 1), finv_(n, 1) {
    init(n);
  }
  constexpr void init(int n) {
    fact_.assign(n, 1), inv_.assign(n, 1), finv_.assign(n, 1);
    int MOD = fact_[0].get_mod();
    for(int i = 2; i < n; i++){
      fact_[i] = fact_[i-1] * i;
      inv_[i] = -inv_[MOD%i] * (MOD/i);
      finv_[i] = finv_[i-1] * inv_[i];
    }
  }
  constexpr mint com(int n, int k) const {
    if (n < k || n < 0 || k < 0) return 0;
    return fact_[n] * finv_[k] * finv_[n-k];
  }
  constexpr mint fact(int n) const {
    if (n < 0) return 0;
    return fact_[n];
  }
  constexpr mint inv(int n) const {
    if (n < 0) return 0;
    return inv_[n];
  }
  constexpr mint finv(int n) const {
    if (n < 0) return 0;
    return finv_[n];
  }
};

using mint = Fp<MOD>;

/* input */
inline void scan(){}
template<class Head,class... Tail>
inline void scan(Head&head,Tail&... tail){std::cin >> head; scan(tail...);}
#define LL(...) long long __VA_ARGS__;scan(__VA_ARGS__)
#define LD(...) long double __VA_ARGS__;scan(__VA_ARGS__)
#define STR(...) string __VA_ARGS__;scan(__VA_ARGS__)
#define CHAR(...) char __VA_ARGS__;scan(__VA_ARGS__)
#define VEC(type, name, size) \
  vector<type> name(size);    \
  for(auto &x: name) cin >> x
#define VEC2(type1, name1, type2, name2, size) \
  vector<type1> name1(size);    \
  vector<type2> name2(size);    \
  rep(i, size) cin >> name1[i] >> name2[i];
#define VEC3(type1, name1, type2, name2, type3, name3, size) \
  vector<type1> name1(size);    \
  vector<type2> name2(size);    \
  vector<type3> name3(size);    \
  rep(i, size) cin >> name1[i] >> name2[i] >> name3[i];
#define VVEC(type, name, h, w) \
  vector<vector<type>> name(h, vector<type>(w)); \
  for(auto &row: name){ \
    for(auto &in: row){ \
      cin >> in; \
    } \
  }

/* print */
// __init128
std::ostream &operator<<(std::ostream &dest, __int128_t value) {
  std::ostream::sentry s(dest);
  if (s) {
    __uint128_t tmp = value < 0 ? -value : value;
    char buffer[128];
    char *d = std::end(buffer);
    do {
      --d;
      *d = "0123456789"[tmp % 10];
      tmp /= 10;
    } while (tmp != 0);
    if (value < 0) {
      --d;
      *d = '-';
    }
    int len = std::end(buffer) - d;
    if (dest.rdbuf()->sputn(d, len) != len) {
      dest.setstate(std::ios_base::badbit);
    }
  }
  return dest;
}
__int128 parse(string &s) {
  __int128 ret = 0;
  for (ll i = 0; i < (ll)s.size(); i++)
    if ('0' <= s[i] && s[i] <= '9')
      ret = 10 * ret + s[i] - '0';
  return ret;
}
void print() {
  cout << endl;
}
template <class Head, class... Tail>
void print(Head&& head, Tail&&... tail) {
  cout << head;
  if (sizeof...(tail) != 0) cout << " ";
  print(forward<Tail>(tail)...);
}
template <class T>
void print(vector<T> &vec) {
  for (auto& a : vec) {
    cout << a;
    if (&a != &vec.back()) cout << " ";
  }
  cout << endl;
}
template <class T>
void print(vector<vector<T>> &df) {
  for (auto& vec : df) {
    print(vec);
  }
}

/* lambda */
template<class F>
struct lambda {
private:
  F func;
public:
  template<class G>
  constexpr lambda(G&& func) noexcept: func(std::forward<G>(func)) {}
  template<class... Args>
  constexpr decltype(auto) operator ()(Args&&... args) const noexcept(std::is_nothrow_invocable_v<F, Args...>) {
    return func(*this, forward<Args>(args)...);
  }
};
template<class G>
lambda(G&&) -> lambda<std::decay_t<G>>;

/* debug */
#ifdef LOCAL
#  include <debug_print.hpp>
#  define debug(...) cerr << "\033[33m"; debug_print::multi_print(#__VA_ARGS__, __VA_ARGS__); cerr << "\033[m";
#else
#  define debug(...) ;
#endif

// Segment Tree
template<class Monoid> struct SegmentTree {
  using Func = function<Monoid(Monoid, Monoid)>;

  // core member
  long long N;
  Func OP;
  Monoid IDENTITY;
  
  // inner data
  long long log, offset;
  vector<Monoid> dat;

  // constructor
  SegmentTree() {}
  SegmentTree(long long n, const Func &op, const Monoid &identity) {
    init(n, op, identity);
  }
  SegmentTree(const vector<Monoid> &v, const Func &op, const Monoid &identity) {
    init(v, op, identity);
  }
  void init(long long n, const Func &op, const Monoid &identity) {
    N = n;
    OP = op;
    IDENTITY = identity;
    log = 0, offset = 1;
    while (offset < N) ++log, offset <<= 1;
    dat.assign(offset * 2, IDENTITY);
  }
  void init(const vector<Monoid> &v, const Func &op, const Monoid &identity) {
    init((long long)v.size(), op, identity);
    build(v);
  }
  void pull(long long k) {
    dat[k] = OP(dat[k * 2], dat[k * 2 + 1]);
  }
  void build(const vector<Monoid> &v) {
    assert(N == (long long)v.size());
    for (long long i = 0; i < N; ++i) dat[i + offset] = v[i];
    for (long long k = offset - 1; k > 0; --k) pull(k);
  }
  long long size() const {
    return N;
  }
  Monoid operator [] (long long i) const {
    return dat[i + offset];
  }
  
  // update A[i], i is 0-indexed, O(log N)
  void set(long long i, const Monoid &v) {
    assert(0 <= i && i < N);
    long long k = i + offset;
    dat[k] = v;
    while (k >>= 1) pull(k);
  }
  
  // get [l, r), l and r are 0-indexed, O(log N)
  Monoid prod(long long l, long long r) {
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
  long long max_right(const function<bool(Monoid)> f, long long l = 0) {
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
  long long min_left(const function<bool(Monoid)> f, long long r = -1) {
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
    for (long long i = 0; i < (long long)seg.size(); ++i) {
      s << seg[i];
      if (i != (long long)seg.size() - 1) s << " ";
    }
    return s;
  }
};

int main(){
  LL(H, W);
  VVEC(ll, A, H, W);
  VVEC(ll, B, H, W);
  vector<ll> vh;
  rep(i, H){
    vh.push_back(i);
  }
  vector<ll> vw;
  rep(i, W){
    vw.push_back(i);
  }
  sort(vh);
  sort(vw);
  vector v(H, vector<ll>(W));
  ll ans = INF;
  do{
    do{
      rep(i, H){
        rep(j, W){
          v[i][j] = A[vh[i]][vw[j]];
        }
      }

      if(v == B){
        // ll cnt = 0;
        // while(1){
        //   bool f = true;
        //   rep(i, H){
        //     if(vh[i] > i){
        //       swap(vh[i], vh[i + 1]);
        //       cnt++;
        //       f = false;
        //     }
        //   }
        //   if(f == true){
        //     break;
        //   }
        // }

        // while(1){
        //   bool f = true;
        //   rep(i, W){
        //     if(vw[i] > i){
        //       swap(vw[i], vw[i + 1]);
        //       cnt++;
        //       f = false;
        //     }
        //   }
        //   if(f == true){
        //     break;
        //   }
        // }
        // chmin(ans, cnt);
        ll cnt = 0;
        vector<ll> v1(H);
        SegmentTree<ll> seg(v1, [&](ll a, ll b){ return a + b; }, 0);
        rep(i, H){
          cnt += seg.prod(vh[i], H);
          seg.set(vh[i], 1);
        }
        vector<ll> v2(W);
        SegmentTree<ll> seg2(v2, [&](ll a, ll b){ return a + b; }, 0);
        rep(i, W){
          cnt += seg2.prod(vw[i], W);
          seg2.set(vw[i], 1);
        }
        chmin(ans, cnt);
      }
    } while (next_permutation(all(vw)));       
  } while (next_permutation(all(vh)));

  if(ans == INF){
    print(-1);
  }else{
    print(ans);
  }
}