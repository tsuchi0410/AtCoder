#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

using ll = long long;
using ull = unsigned long long;
using ld = long double;
// cout << fixed << setprecision(10);
const ll INF = 9223372036854775807;
const ld PI = acos(-1);

#define pb push_back
#define eb emplace_back
#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define elif else if
#define add insert

#define ctoll(x) static_cast<long long>(x - '0')
#define lltos(x) to_string(x)
#define lltoc(x) static_cast<char>(x + '0')

#define all(v) (v).begin(),(v).end()
#define len(v) ll(v.size())
#define MIN(v) *min_element(all(v))
#define MAX(v) *max_element(all(v))
template <typename T>
T SUM(const vector<T> &v) {
    T total = 0;
    for(int i = 0; i < len(v); i++) total += v[i];
    return total;
}

#define OVERLOAD_SORT(_1, _2, name, ...) name
#define SORT1(x) stable_sort((x).begin(), (x).end())
#define SORT2(x, idx) stable_sort(all(x), [&](const vector<long long> &_a_, const vector<long long> &_b_){return _a_[idx] < _b_[idx];})
#define SORT(...) OVERLOAD_SORT(__VA_ARGS__, SORT2, SORT1)(__VA_ARGS__)
#define OVERLOAD_RSORT(_1, _2, name, ...) name
#define RSORT1(x) stable_sort((x).rbegin(), (x).rend())
#define RSORT2(x, idx) stable_sort((x).rbegin(), (x).rend(), [&](const vector<long long> &_a_, const vector<long long> &_b_){return _a_[idx] < _b_[idx];})
/*
#define RSORT2(x, idx) stable_sort((x).rbegin(), (x).rend(), [&](const vector<long long> &_a_, const vector<long long> &_b_){ \
    if (_a_[1] == _b_[1]) { \
        return _a_[0] > _b_[0]; \
    } \
    return _a_[1] < _b_[1]; })
*/
#define RSORT(...) OVERLOAD_RSORT(__VA_ARGS__, RSORT2, RSORT1)(__VA_ARGS__)

template <class T>
void rev(T &v) {
  reverse((v).begin(), (v).end());
}
#define uniq(v) \
    SORT(v), v.erase(unique(all(v)), v.end()), v.shrink_to_fit()
template<typename T>
void chmin(T& a, T b) {
  a = min(a, b);
}
template<typename T>
void chmax(T& a, T b) {
  a = max(a, b);
}
template<class T> bool contain(const std::string& s, const T& v) {
return s.find(v) != std::string::npos;
}

#define OVERLOAD_REP(_1, _2, _3, _4, name, ...) name
#define REP1(i, n) for (auto i = std::decay_t<decltype(n)>{}; (i) != (n); ++(i))
#define REP2(i, l, r) for (auto i = (l); (i) != (r); ++(i))
#define REP3(i, l, r, s) for (auto i = (l); (i) < (ll)(r); (i) += s)
#define rep(...) OVERLOAD_REP(__VA_ARGS__, REP3, REP2, REP1)(__VA_ARGS__)
#define rrep(i, a, b) for(int i = a; i >= b; i--)
#define OVERLOAD_FORE(_1, _2, _3, name, ...) name
#define FORE1(i, a) for(auto &i : a)
#define FORE2(i, j, a) for(auto &[i, j] : a)
#define fore(...) OVERLOAD_FORE(__VA_ARGS__, FORE2, FORE1)(__VA_ARGS__)

using vl = vector<ll>;
using vvl = vector<vector<ll>>;
using vvvl = vector<vector<vector<ll>>>;
using vs = vector<string>;
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
using pq = priority_queue<T>;
template <class T>
using pqg = priority_queue<T, vector<T>, greater<T>>;  // 昇順
// unordered_set, unordered_multiset, unordered_map, unordered_multimap で pair, vector, tuple を key に設定させる
template<class T> size_t HashCombine(const size_t seed,const T &v){
    return seed^(std::hash<T>()(v)+0x9e3779b9+(seed<<6)+(seed>>2));
}
/* pair用 */
template<class T,class S> struct std::hash<std::pair<T,S>>{
    size_t operator()(const std::pair<T,S> &keyval) const noexcept {
        return HashCombine(std::hash<T>()(keyval.first), keyval.second);
    }
};
/* vector用 */
template<class T> struct std::hash<std::vector<T>>{
    size_t operator()(const std::vector<T> &keyval) const noexcept {
        size_t s=0;
        for (auto&& v: keyval) s=HashCombine(s,v);
        return s;
    }
};
/* tuple用 */
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

// bisect
// vector
template <typename T>
int bisect_left(vector<T> &X, T v){
  return lower_bound(X.begin(), X.end(), v) - X.begin();
}
template <typename T>
int bisect_right(vector<T> &X, T v){
  return upper_bound(X.begin(), X.end(), v) - X.begin();
}
// set
template <typename T>
T set_bisect_left(set<T> &X, T v){
  auto itr = X.lower_bound(v);
  T obj = *itr;
  return obj;
}
template <typename T>
T set_bisect_right(set<T> &X, T v){
  auto itr = X.upper_bound(v);
  T obj = *itr;
  return obj;
}
// multiset
template <typename T>
T mset_bisect_left(mset<T> &X, T v){
  auto itr = X.lower_bound(v);
  T obj = *itr;
  return obj;
}
template <typename T>
T mset_bisect_right(mset<T> &X, T v){
  auto itr = X.upper_bound(v);
  T obj = *itr;
  return obj;
}
// map
template <typename T, typename U>
pair<T, U> map_bisect_left(map<T, U> &X, T v){
  auto itr = X.lower_bound(v);
  pair<T, U> obj = *itr;
  return obj;
}
template <typename T, typename U>
pair<T, U> map_bisect_right(map<T, U> &X, T v){
  auto itr = X.upper_bound(v);
  pair<T, U> obj = *itr;
  return obj;
}

// input
inline void scan(){}
template<class Head,class... Tail>
inline void scan(Head&head,Tail&... tail){std::cin >> head; scan(tail...);}
#define LL(...) long long __VA_ARGS__;scan(__VA_ARGS__)
#define LD(...) long double __VA_ARGS__;scan(__VA_ARGS__)
#define STR(...) string __VA_ARGS__;scan(__VA_ARGS__)
#define CHAR(...) char __VA_ARGS__;scan(__VA_ARGS__)
// vector
template <typename T>
istream &operator>>(istream &is, vector<T> &v)
{
  for (T &in : v)
  is >> in;
  return is;
}

// print
void print() {
  cout << endl;
}
template <class Head, class... Tail>
void print(Head&& head, Tail&&... tail) {
  cout << head;
  if (sizeof...(tail) != 0) cout << " ";
  print(forward<Tail>(tail)...);
}

#ifdef LOCAL
#   include <debug_print.hpp>
#   define debug(...) cerr << "\033[33m"; debug_print::multi_print(#__VA_ARGS__, __VA_ARGS__); cerr << "\033[m";
#else
#   define debug(...) ;
#endif



int main(){
    LL(N);
    vl T(N);
    cin >> T;
    ll M = 100010;
    vvl dp(N, vl(M));
    rep(i, N){
        rep(j, M){
            if(T[i] == j){
                dp[i][j] = 1;
            }
            if(dp[i][j] == 0){
                continue;
            }
            if(i == N - 1){
                continue;
            }
            dp[i + 1][j + 1] = 1;
            dp[i + 1][j + T[i + 1]] = 1;
        }
    }
    ld ans = 10000000000;
    ld cnt = (ld)SUM(T) / (ld)2;

    rep(i, M){
        if(dp[N - 1][i] == 1){
            if(i < cnt){
                chmin(ans, cnt + cnt - i);
            }else{
                chmin(ans, (ld)i);
            }
        }
    }
    debug(ans);
    debug(SUM(T));
    print(max((ll)ans, (ll)SUM(T) - (ll)ans));
}