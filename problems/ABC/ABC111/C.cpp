#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ull = unsigned long long;
using ld = long double;
// setprecision()
const ll INF = 9223372036854775807;

#define pb push_back
#define eb emplace_back
// #define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define elif else if

#define all(v) (v).begin(),(v).end()
#define len(v) ll(v.size())
#define MIN(v) *min_element(all(v))
#define MAX(v) *max_element(all(v))

#define OVERLOAD_SORT(_1, _2, name, ...) name
#define SORT1(x) stable_sort((x).begin(), (x).end())
#define SORT2(x, idx) stable_sort(all(x), [&](const vector<long long> &_a_, const vector<long long> &_b_){return _a_[idx] < _b_[idx];})
#define sort(...) OVERLOAD_SORT(__VA_ARGS__, SORT2, SORT1)(__VA_ARGS__)
#define OVERLOAD_RSORT(_1, _2, name, ...) name
#define RSORT1(x) stable_sort((x).rbegin(), (x).rend())
#define RSORT2(x, idx) stable_sort((x).rbegin(), (x).rend(), [&](const vector<long long> &_a_, const vector<long long> &_b_){return _a_[idx] < _b_[idx];})
#define rsort(...) OVERLOAD_RSORT(__VA_ARGS__, RSORT2, RSORT1)(__VA_ARGS__)

template <class T>
void reverse(T &v) {
  reverse((v).begin(), (v).end());
}
#define uniq(x) \
  v.erase(unique(all(v)), v.end()), v.shrink_to_fit()
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
#define repset(i, a) for(auto &i : a)
#define repmap(i, j, a) for(auto &[i, j] : a)

using vl = vector<ll>;
using vvl = vector<vector<ll>>;
using vs = vector<string>;
template <typename T>
using uset = unordered_set<T>;
template <typename T>
using mset = multiset<T>;
#define discard(s, x) {auto itr_ = s.find((x)); if (itr_ != s.end()) s.erase(itr_); }
template <typename T, typename U>
using umap = unordered_map<T, U>;
template <class T>
using pq = priority_queue<T>;
template <class T>
using pqg = priority_queue<T, vector<T>, greater<T>>;

// bisect
template <typename T>
int bisect_left(vector<T> &X, T v){
  return lower_bound(X.begin(), X.end(), v) - X.begin();
}
template <typename T>
int bisect_right(vector<T> &X, T v){
  return upper_bound(X.begin(), X.end(), v) - X.begin();
}

// input
// vector
template <typename T>
istream &operator>>(istream &is, vector<T> &v)
{
  for (T &in : v)
    is >> in;
  return is;
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
template <class T>
void print(set<T> &s) {
  for (auto it = s.begin(); it != s.end(); ++it) {
  cout << *it;
  if (next(it) != s.end()) cout << " ";
  }
  cout << endl;
}
template <class T>
void print(unordered_set<T> &us) {
  for (auto it = us.begin(); it != us.end(); ++it) {
  cout << *it;
  if (next(it) != us.end()) cout << " ";
  }
  cout << endl;
}
template <class T>
void print(multiset<T> &s) {
  for (auto it = s.begin(); it != s.end(); ++it) {
  cout << *it;
  if (next(it) != s.end()) cout << " ";
  }
  cout << endl;
}
template <class Key, class Value>
void print(map<Key, Value> &m) {
  for (auto it = m.begin(); it != m.end(); ++it) {
  cout << it->first << " " << it->second << endl;
  }
}
template <class Key, class Value>
void print(unordered_map<Key, Value> &um) {
  for (auto it = um.begin(); it != um.end(); ++it) {
  cout << it->first << " " << it->second << endl;
  }
}



int main(){
    ll N;
    cin >> N;
    vl v(N);
    cin >> v;
    
    map<ll, ll> m1, m2;
    rep(i, N){
        if(i % 2 == 0) m1[v[i]]++;
        else m2[v[i]]++;
    }
    vvl cnt1, cnt2;
    repmap(k, v, m1){
        vl a = {k, v};
        cnt1.pb(a);
    }
    repmap(k, v, m2){
        vl a = {k, v};
        cnt2.pb(a);
    }
    
    rsort(cnt1, 1);
    rsort(cnt2, 1);

    if(cnt1[0][0] != cnt2[0][0]){
        ll ans = 0;
        ans += (N / 2) - cnt1[0][1];
        ans += (N / 2) - cnt2[0][1];
        print(ans);
    }else{
        ll ans1 = 0;
        if(len(cnt1) == 1){
            ans1 += cnt1[0][1];
        }else{
            ans1 += (N / 2) - cnt1[1][1];
        }
        ans1 += (N / 2) - cnt2[0][1];

        ll ans2 = 0;
        ans2 += (N / 2) - cnt1[0][1];
        if(len(cnt2) == 1){
            ans2 += cnt2[0][1];
        }else{
            ans2 += (N / 2) - cnt2[1][1];
        }
        print(min(ans1, ans2));
    }
}