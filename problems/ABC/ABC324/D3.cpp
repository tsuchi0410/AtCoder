#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

// 型, 定数
using ll = long long;
using ull = unsigned long long;
using ld = long double;
// cout << fixed << setprecision(10);
const ll INF = 4e18;
const ld PI = acos(-1);

// 省略
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define elif else if
#define add insert

// 独自関数
#define ctoll(x) static_cast<long long>(x - '0')
#define lltos(x) to_string(x)
#define lltoc(x) static_cast<char>(x + '0')
#define minvec(v) *min_element(all(v))
#define maxvec(v) *max_element(all(v))
#define minset(st) *(st.begin())
#define maxset(st) *(--st.end())
#define minmap(m) *(m.begin())
#define maxmap(m) *(--m.end())
#define all(v) (v).begin(),(v).end()
#define len(v) ll(v.size())
/* vector の contains 判定*/
template <typename T, typename U>
bool exist(const vector<T>& v, const U& x){
    auto it = find(v.begin(), v.end(), x) ;
    return it != v.end();
}
/* vector の合計 */
template <typename T>
T SUM(const vector<T> &v) {
    T total = 0;
    for(int i = 0; i < len(v); i++) total += v[i];
    return total;
}
/* string, vector の反転*/
template <class T>
void rev(T &v) {
  reverse((v).begin(), (v).end());
}
/* uniq := sorted(list(set(v)))*/
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

// ソート
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

// ループ
#define OVERLOAD_REP(_1, _2, _3, _4, name, ...) name
#define REP1(i, n) for (ll i = 0; i != n; ++i)
#define REP2(i, l, r) for (ll i = l; i != r; ++i)
#define REP3(i, l, r, s) for (ll i = l; i < r; i += s)
#define rep(...) OVERLOAD_REP(__VA_ARGS__, REP3, REP2, REP1)(__VA_ARGS__)
#define OVERLOAD_RREP(_1, _2, _3, _4, name, ...) name
#define RREP1(i, n) for (ll i = n; i != -1; --i)
#define RREP2(i, l, r) for (ll i = l; i != r; --i)
#define RREP3(i, l, r, s) for (ll i = l; i > r; i -= s)
#define rrep(...) OVERLOAD_RREP(__VA_ARGS__, RREP3, RREP2, RREP1)(__VA_ARGS__)
#define OVERLOAD_FORE(_1, _2, _3, name, ...) name
#define FORE1(i, a) for(auto &i : a)
#define FORE2(i, j, a) for(auto &[i, j] : a)
#define fore(...) OVERLOAD_FORE(__VA_ARGS__, FORE2, FORE1)(__VA_ARGS__)

// コンテナ
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
// 多次元 vector 生成
template<class T, size_t n, size_t idx = 0>
auto makevec(const size_t (&d)[n], const T& init) noexcept {
    if constexpr (idx < n) return std::vector(d[idx], makevec<T, n, idx + 1>(d, init));
    else return init;
}
template<class T, size_t n>
auto makevec(const size_t (&d)[n]) noexcept {
    return makevec(d, T{});
}

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

// bisect (vector)
template <typename T>
int bisect_left(vector<T> &X, T v){
  return lower_bound(X.begin(), X.end(), v) - X.begin();
}
template <typename T>
int bisect_right(vector<T> &X, T v){
  return upper_bound(X.begin(), X.end(), v) - X.begin();
}

// input
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
#define VVEC(type, name, h, w) \
    vector<vector<type>> name(h, vector<type>(w)); \
    for(auto &row: name){ \
        for(auto &in: row){ \
            cin >> in; \
        } \
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

// lambda
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

// debug
#ifdef LOCAL
#   include <debug_print.hpp>
#   define debug(...) cerr << "\033[33m"; debug_print::multi_print(#__VA_ARGS__, __VA_ARGS__); cerr << "\033[m";
#else
#   define debug(...) ;
#endif



int main(){
    LL(N);
    STR(S);
    
    umap<char, ll> dic1;
    rep(i, 10) dic1[lltoc(i)] = 0;
    fore(i, S) dic1[i]++;

    ll cnt = 0;
    rep(i, 10000001){
        ll x = i * i;
        string x2 = lltos(x);

        umap<char, ll> dic2;
        rep(i, 10) dic2[lltoc(i)] = 0;
        fore(i, x2) dic1[i]++;
        
        umap<char, ll> dic3;
        fore(k, v, dic1){
            dic3[k] = dic1[k] - dic2[k];
        }

        bool f = true;
        fore(k, v, dic3){
            if(k == '0'){
                if(dic1[k] < dic2[k]){
                    f = false;
                    break;
                }
            }
            if(v != 0){
                f = false;
                break;
            }
        }
        if(f == true) cnt++;
    }
    print(cnt);
}