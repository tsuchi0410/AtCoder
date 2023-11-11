#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

/* 型, 定数 */
using ll = long long;
using ull = unsigned long long;
using i128 = __int128;
using ld = long double;
// cout << fixed << setprecision(10);
const ll INF = 1e18;
const ld PI = acos(-1);
const ll MOD = 998244353;
using mint = atcoder::modint998244353;
// const ll MOD = 1000000007;
// using mint = atcoder::modint1000000007;

/* 省略 */
#define pb push_back
#define elif else if

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
#define sum(...) accumulate(all(__VA_ARGS__),0LL)
template <typename T> vector<T> cum(vector<T> &v){ vector<T> s = {0}; for(ll i = 0; i < (ll)v.size(); i++) s.push_back(s[i] + v[i]); return s; }
ll powll(ll n, ll r){ if (r == 0) return 1; else if (r % 2 == 0) return powll(n * n, (ll)(r / 2)); else return n * powll(n, r - 1); }
template<class T, class U> ll count(const T& a, const U& b){ return count(all(a), b); }
template <typename T> unordered_map<T, ll> ucounter(vector<T> &v){ unordered_map<T, ll> mp; for(ll i = 0; i < (ll)v.size(); i++) mp[v[i]]++; return mp; }
template <typename T> map<T, ll> counter(vector<T> &v){ map<T, ll> mp; for(ll i = 0; i < (ll)v.size(); i++) mp[v[i]]++;
return mp; }
template <typename T, typename U> bool exist(const vector<T>& v, const U& x){ auto it = find(v.begin(), v.end(), x); return it != v.end(); }
template <typename T> vector<T> join(const vector<T> &v1, const vector<T> &v2) { vector<T> v3 = v1; v3.insert(v3.end(), all(v2)); return v3; }
template <typename T, typename U> T index(const vector<T> &v, U x) { for(ll i = 0; i < len(v); i++) if(v[i] == x) return i; return -1; }
#define reverse(v) reverse(all(v))
#define unique(v) sort(all(v)), v.erase(unique(all(v)), v.end()), v.shrink_to_fit()
template<typename T> void chmin(T& a, T b) { a = min(a, b); }
template<typename T> void chmax(T& a, T b) { a = max(a, b); }
template <typename T> ll bisect_left(vector<T> &X, ll v){ return lower_bound(X.begin(), X.end(), (ll)v) - X.begin(); }
template <typename T> ll bisect_right(vector<T> &X, ll v){ return upper_bound(X.begin(), X.end(), (ll)v) - X.begin(); }

/* ソート */
#define OVERLOAD_SORT(_1, _2, name, ...) name
#define SORT1(x) stable_sort((x).begin(), (x).end())
#define SORT2(x, idx) stable_sort(all(x), [&](const vector<long long> &_a_, const vector<long long> &_b_){return _a_[idx] < _b_[idx];})
#define SORT(...) OVERLOAD_SORT(__VA_ARGS__, SORT2, SORT1)(__VA_ARGS__)
#define OVERLOAD_RSORT(_1, _2, name, ...) name
#define RSORT1(x) stable_sort((x).rbegin(), (x).rend())
#define RSORT2(x, idx) stable_sort((x).rbegin(), (x).rend(), [&](const vector<long long> &_a_, const vector<long long> &_b_){return _a_[idx] < _b_[idx];})
#define RSORT(...) OVERLOAD_RSORT(__VA_ARGS__, RSORT2, RSORT1)(__VA_ARGS__)

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
using vl = vector<ll>;
using vvl = vector<vector<ll>>;
using vvvl = vector<vector<vector<ll>>>;
template <typename T>
using uset = unordered_set<T>;
template <typename T>
using mset = multiset<T>;
#define discard(s, x) {auto itr_ = s.find((x)); if (itr_ != s.end()) s.erase(itr_); }
template <typename T, typename U>
using mmap = multimap<T, U>;
template <typename T, typename U>
using umap = unordered_map<T, U>;
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
// mint
ostream& operator<< (ostream& os,const mint& x){
  return os << x.val();
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



int main(){
  LL(N, M, K, S, T, X);
  vector<vector<ll>> G(N + 1);
  rep(i, M){
    LL(u, v);
    G[u].push_back(v);
    G[v].push_back(u);
  }

  vector dp(K + 1, vector(N + 1, vector<mint>(2)));
  dp[0][S][0] = 1;
  rep(i, K){
    rep(v, N + 1){
      rep(k, 2){
        fore(u, G[v]){
          if(u == X){
            dp[i + 1][u][k ^ 1] += dp[i][v][k];
          }else{
            dp[i + 1][u][k] += dp[i][v][k];
          }
        }
      }
    }
  }
  debug(dp)
  print(dp[K][T][0]);
}