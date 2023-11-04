#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

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

/* 型, 定数 */
using ll = long long;
using ull = unsigned long long;
using ld = long double;
// cout << fixed << setprecision(10);
const ll INF = 1e18;
const ld PI = acos(-1);
using mint = atcoder::modint998244353;
// using mint = atcoder::modint1000000007;

/* 省略 */
#define pb push_back
#define eb emplace_back
// #define mp make_pair
// #define mt make_tuple
#define fi first
#define se second
#define elif else if
#define add insert
#define del erase

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
template <typename T> vector<T> cum(vector<T> &v){ vector<T> s = {0}; for(ll i = 0; i < v.size(); i++) s.push_back(s[i] + v[i]); return s; }
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
using vs = vector<string>;
using vb = vector<bool>;
using vm = vector<mint>;
using vvm = vector<vm>;
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
#   include <debug_print.hpp>
#   define debug(...) cerr << "\033[33m"; debug_print::multi_print(#__VA_ARGS__, __VA_ARGS__); cerr << "\033[m";
#else
#   define debug(...) ;
#endif



int main(){
  LL(N);
  STR(R, C);

  itertools I;
  vl v;
  rep(i, N){
    v.pb(i);
  }
  vvl perm = I.permutations(v);

  rep(i, len(perm)){
    rep(j, len(perm)){
      rep(k, len(perm)){
        if(i == j or j == k or k == i){
          continue;
        }
        vector<vector<char>> masu(N, vector<char>(N, '.'));
        rep(l, N){
          masu[l][perm[i][l]] = 'A';
          masu[l][perm[j][l]] = 'B';
          masu[l][perm[k][l]] = 'C';
        }
        
        bool f = true;
        rep(l, N){
          rep(m, N){
            if(masu[l][m] == '.'){
              continue;
            }
            if(masu[l][m] == R[l]){
              break;
            }else{
              f = false;
              break;
            }
          }
        }

        rep(m, N){
          rep(l, N){
            if(masu[l][m] == '.'){
              continue;
            }
            if(masu[l][m] == C[m]){
              break;
            }else{
              f = false;
              break;
            }
          }
        }

        rep(l, N){
          uset<ll> s;
          rep(m, N){
            s.add(masu[l][m]);
          }
          if(s.contains('A') and s.contains('B') and s.contains('C')){
            ;
          }else{
            f = false;
          }
        }

        rep(m, N){
          uset<ll> s;
          rep(l, N){
            s.add(masu[l][m]);
          }
          if(s.contains('A') and s.contains('B') and s.contains('C')){
            ;
          }else{
            f = false;
          }
        }

        if(f){
          print("Yes");
          rep(i, N){
            rep(j, N){
              cout << masu[i][j];
            }
            cout << endl;
          }
          return 0;
        }

      }
    }
  }

  print("No");
}