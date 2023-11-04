#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

using ll = long long;
using ull = unsigned long long;
using ld = long double;
// cout << fixed << setprecision(10);
const ll INF = 4e18;
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
ll bisect_left(vector<T> &X, T v){
  return lower_bound(X.begin(), X.end(), v) - X.begin();
}
template <typename T>
ll bisect_right(vector<T> &X, T v){
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

#ifdef LOCAL
#   include <debug_print.hpp>
#   define debug(...) cerr << "\033[33m"; debug_print::multi_print(#__VA_ARGS__, __VA_ARGS__); cerr << "\033[m";
#else
#   define debug(...) ;
#endif

vvl vec = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

int main(){
    LL(H, W);
    VEC(string, A, H);
    debug(A);
    ll sh, sw, gh, gw;
    umap<ll, vl> dhu, dhd, dhr, dhl, dwu, dwd, dwr, dwl, dhrock, dwrock;
    rep(i, H){
        rep(j, W){
            if(A[i][j] == 'S'){
                sh = i;
                sw = j;
            }elif(A[i][j] == 'G'){
                gh = i;
                gw = j;
            }elif(A[i][j] == '#'){
                dhrock[i].pb(j);
                dwrock[j].pb(i);
            }elif(A[i][j] == '^'){
                dhu[i].pb(j);
                dwu[j].pb(i);
            }elif(A[i][j] == '>'){
                dhr[i].pb(j);
                dwr[j].pb(i);
            }elif(A[i][j] == 'v'){
                dhd[i].pb(j);
                dwd[j].pb(i);
            }elif(A[i][j] == '<'){
                dhl[i].pb(j);
                dwl[j].pb(i);
            }
        }
    }
    fore(k, v, dhu){
        dhu[k].pb(INF);
        dhu[k].pb(-1 * INF);
        SORT(dhu[k]);
    }
    fore(k, v, dhl){
        dhl[k].pb(INF);
        dhl[k].pb(-1 * INF);
        SORT(dhl[k]);
    }
    fore(k, v, dhd){
        dhd[k].pb(INF);
        dhd[k].pb(-1 * INF);
        SORT(dhd[k]);
    }
    fore(k, v, dhr){
        dhr[k].pb(INF);
        dhr[k].pb(-1 * INF);
        SORT(dhr[k]);
    }
    fore(k, v, dwu){
        dwu[k].pb(INF);
        dwu[k].pb(-1 * INF);
        SORT(dwu[k]);
    }
    fore(k, v, dwl){
        dwl[k].pb(INF);
        dwl[k].pb(-1 * INF);
        SORT(dwl[k]);
    }
    fore(k, v, dwd){
        dwd[k].pb(INF);
        dwd[k].pb(-1 * INF);
        SORT(dwd[k]);
    }
    fore(k, v, dwr){
        dwr[k].pb(INF);
        dwr[k].pb(-1 * INF);
        SORT(dwr[k]);
    }
    fore(k, v, dhrock){
        dhrock[k].pb(INF);
        dhrock[k].pb(-1 * INF);
        SORT(dhrock[k]);
    }
    fore(k, v, dwrock){
        dwrock[k].pb(INF);
        dwrock[k].pb(-1 * INF);
        SORT(dwrock[k]);
    }

    }
    vvl d(H, vl(W, -1));
    d[sh][sw] = 0;
    queue<vl> q;
    q.push({sh, sw});
    while(len(q)){
        ll y = q.front()[0];
        ll x = q.front()[1];
        q.pop();
        if((y == gh) and (x == gw)){
            break;
        }
        rep(i, len(vec)){
            ll ny = y + vec[i][0];
            ll nx = x + vec[i][1];
            if((ny < 0) or (nx < 0)){
                continue;
            }
            if((ny >= H) or (nx >= W)){
                continue;
            }
            bool f = true;
            // 横に移動
            if(vec[i][0] == 0){
                if(dwu.contains(nx)){
                    ll nup;
                    ll idx = bisect_left(dwu[nx], ny);
                    if(dwu[nx][idx] != INF){
                        nup = dwu[nx][idx];
                        f = false;
                    }
                    if(dwrock.contains(nx)){
                        ll idx1 = bisect_left(dwrock[nx], ny);
                        ll idx2 = bisect_left(dwrock[nx], nup);
                        if(idx1 != idx2){
                            f = true;
                        }
                    }
                }
                if(dwd.contains(nx)){
                    debug("ok");
                    ll ndown;
                    ll idx = bisect_left(dwd[nx], ny);
                    idx--;
                    if(dwd[nx][idx] != -1 * INF){
                        ndown = dwd[nx][idx];
                        f = false;
                    }
                    if(dwrock.contains(nx)){
                        ll idx1 = bisect_left(dwrock[nx], ny);
                        ll idx2 = bisect_left(dwrock[nx], ndown);
                        if(idx1 != idx2){
                            f = true;
                        }
                    }
                }
            }
            if((d[ny][nx] == -1) and (A[ny][nx] == '.') and (f == true)){
                q.push({ny, nx});
                d[ny][nx] = d[y][x] + 1;
            }
        }
    }
    debug(d)
    debug(dwd);
}