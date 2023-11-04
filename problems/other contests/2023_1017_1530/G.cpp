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
// bisect (vector)
template <typename T>
int bisect_left(vector<T> &X, T v){
  return lower_bound(X.begin(), X.end(), v) - X.begin();
}
template <typename T>
int bisect_right(vector<T> &X, T v){
  return upper_bound(X.begin(), X.end(), v) - X.begin();
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

class itertools{
public:
    //----------------------------combinations---------------------------    
    vector<vector<long long>> combinations(vector<long long> lis,long long repeat){
        long long cnt=0;
        deque<set<long long>> d;
        set<long long> s,tmp;
        d.push_back(s);
        while (cnt<repeat){
            deque<set<long long>> d2;
            for(auto itr=d.begin(); itr!=d.end(); itr++){
                for(auto it=lis.begin()+cnt; it!=lis.begin()+lis.size()+cnt-repeat+1 ; it++){
                    tmp=*itr;
                    tmp.insert(*it);
                    if (tmp.size()==cnt+1){
                        d2.push_back(tmp);
                    }
                }
            }
            d=d2;
            cnt++;
        }
        sort(d.begin(), d.end());
        decltype(d)::iterator result = unique(d.begin(), d.end());
        d.erase(result, d.end());
        vector<vector<long long>> ans;
        for(auto item:d){
            vector<long long> ite(item.begin(),item.end());
            ans.push_back(ite);
        }
        return ans;
    }
    //----------------------------combinations---------------------------

    //----------------------------permutations---------------------------
    vector<vector<long long>> permutations(vector<long long> lis){
        vector<long long> range,tmp(lis.size(),0);
        vector<vector<long long>> ans;

        for(long long i=0  ;i<lis.size()  ;i++){
            range.push_back(i);
        }

        do{
            for(long long i=0  ;i<lis.size()  ;i++){
                tmp[range[i]]=lis[i];
            }
            ans.push_back(tmp);
        }while (next_permutation(range.begin(), range.end()));
        return ans;
    }
    //----------------------------permutations---------------------------

    //------------------------------product------------------------------
    vector<vector<long long>> ary;
    vector<long long> lis;
    vector<long long> tmp;

    void repeating (vector<long long> nums ,vector<long long> lis ,long long repeat){
        if (lis.size()==repeat){
            ary.push_back(lis);
        }else{
            tmp=lis;
            for (auto item:nums){
                tmp.push_back(item);
                repeating(nums,tmp,repeat);
                tmp=lis;
            }
        }
    }

    vector<vector<long long>> product(vector<long long> nums,long long repeat){
        repeating(nums,lis,repeat);
        return ary;
    //------------------------------product------------------------------
    };
};

int main(){
    LL(N, M);
    VEC(string, S, N);
    VEC(string, T, M);

    uset<string> check;
    rep(i, M) check.add(T[i]);

    if(len(S) == 1){
        rep(i, N){
            if(check.contains(S[i]) == false){
                if(3 <= len(S[i]) and len(S[i]) <= 16){
                    print(S[i]);
                    return 0;
                }
            }
        }
        print(-1);
        return 0;
    }

    itertools I;
    ll c = 0;
    rep(i, N){
        c += len(S[i]);
    }
    ll d = 16 - c;
    ll bar = len(S) - 1;
    vl v;
    rep(i, 1, d){
        v.pb(i);
    }
    vvl pro = I.product(v, bar);
    vvl ubsize;
    rep(i, len(pro)){
        ll cnt = 0;
        rep(j, len(pro[i])){
            cnt += pro[i][j];
        }
        if(3 <= len(S) + cnt and len(S) + cnt <= 16){
            ubsize.pb(pro[i]);
        }
    }

    vs ub;
    rep(i, 16){
        string o;
        rep(j, i){
            o += "_";
        }
        ub.pb(o);
    }
    SORT(S);
    do{
        rep(cnt, len(ubsize)){
            string moji;
            rep(i, N){
                moji += S[i];
                if(i != N - 1){
                    moji += ub[ubsize[cnt][i]];
                }
            }
            if(check.contains(moji) == false){
                if(3 <= len(moji) and len(moji) <= 16){
                    print(moji);
                    return 0;
                }
            }
        }
    } while (next_permutation(all(S)));

    print(-1);

}