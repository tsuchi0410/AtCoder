#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ull = unsigned long long;
using ld = long double;

#define pb push_back
#define eb emplace_back
// #define mp make_pair
#define mt make_tuple
#define fi first
#define se second

#define all(v) (v).begin(),(v).end()
#define len(v) ll(v.size())
#define MIN(v) *min_element(all(v))
#define MAX(v) *max_element(all(v))
#define uniq(x) \
    v.erase(unique(all(v)), v.end()), v.shrink_to_fit()
template <class T, class S>
inline bool chmax(T &a, const S &b) {
    return (a < b ? a = b, 1 : 0);
}
template <class T, class S>
inline bool chmin(T &a, const S &b) {
    return (a > b ? a = b, 1 : 0);
}
#define elif else if

#define OVERLOAD_REP(_1, _2, _3, name, ...) name
#define REP1(i, n) for (auto i = std::decay_t<decltype(n)>{}; (i) != (n); ++(i))
#define REP2(i, l, r) for (auto i = (l); (i) != (r); ++(i))
#define rep(...) OVERLOAD_REP(__VA_ARGS__, REP2, REP1)(__VA_ARGS__)
#define rrep(i, a, b) for(int i = a; i >= b; i--)
#define for1(i, a) for(auto &i : a)
#define for2(i, j, a) for(auto &[i, j] : a)

using vl = vector<ll>;
using vvl = vector<vector<ll>>;
using vs = vector<string>;
template <typename T>
using uset = unordered_set<T>;
template <typename T>
using mset = multiset<T>;
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
    ll now = 0;
    rep(i, N){
    ll a;
    cin >> a;
    now >>= a;
    now += 1;
    if (now%2 == 0) ++now;
    now <<= a;
    print(now);
    }
    cout << now << endl;
}