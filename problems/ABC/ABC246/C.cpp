#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ull = unsigned long long;

#define pb push_back
#define eb emplace_back
#define mp make_pair
#define mt make_tuple
#define fi first
#define se second

#define all(x) (x).begin(),(x).end()
#define len(x) ll(x.size())
#define elif else if

#define OVERLOAD_REP(_1, _2, _3, name, ...) name
#define REP1(i, n) for (auto i = std::decay_t<decltype(n)>{}; (i) != (n); ++(i))
#define REP2(i, l, r) for (auto i = (l); (i) != (r); ++(i))
#define rep(...) OVERLOAD_REP(__VA_ARGS__, REP2, REP1)(__VA_ARGS__)
#define rrep(i, a, b) for(int i = a; i >= b; i--)
#define for1(i, a) for(auto &i : a)
#define for2(i, j, a) for(auto &[i, j] : a)

using vl = vector<ll>;
using vs = vector<string>;
template <typename T>
using uset = unordered_set<T>;
template <typename T, typename U>
using umap = unordered_map<T, U>;
template <class T>
using pq = priority_queue<T>;
template <class T>
using pqg = priority_queue<T, vector<T>, greater<T>>;

template <typename T>
int bisect_left(vector<T> &X, T v){
    return lower_bound(X.begin(), X.end(), v) - X.begin();
}
template <typename T>
int bisect_right(vector<T> &X, T v){
    return upper_bound(X.begin(), X.end(), v) - X.begin();
}


// debug
// vector
template<typename T>
ostream& operator << (ostream& os, vector<T>& vec){
    os << "[";
    for(int i = 0; i < vec.size(); i++){
        os << vec[i] << (i + 1 == vec.size() ? "" : ", " );
    }
    os << "]";
    return os;
}
// map
template<typename T, typename U>
ostream& operator << (ostream& os, map<T, U>& mp) {
	os << "{";
	for (auto itr = mp.begin(); itr != mp.end(); itr++) {
		os << "(" << itr->first << ", " << itr->second << ")";
		itr++;
		if(itr != mp.end()) os << ", ";
		itr--;
	}
	os << "}";
	return os;
}
// unordered_map
template<typename T, typename U>
ostream& operator << (ostream& os, unordered_map<T, U>& ump) {
	os << "{";
    int cnt = 0;
    for (auto itr = ump.begin(); itr != ump.end(); itr++) {
            os << "(" << itr->first << " => " << itr->second << ")";
            cnt++;
            if(cnt != ump.size()){
                os << ", ";
            }
        }
	os << "}";
	return os;
}
// set
template<typename T>
ostream& operator << (ostream& os, set<T>& st) {
	os << "{";
	for (auto itr = st.begin(); itr != st.end(); itr++) {
		os << *itr;
		++itr;
		if(itr != st.end()) os << ", ";
		itr--;
	}
	os << "}";
	return os;
}
// unordered_set
template<typename T>
ostream& operator << (ostream& os, unordered_set<T>& ust) {
	os << "{";
    int cnt = 0;
	for (auto itr = ust.begin(); itr != ust.end(); itr++) {
		os << *itr;
		cnt++;
        if(cnt != ust.size()){
            os << ", ";
        }
	}
	os << "}";
	return os;
}

int main(){
    ll N, K, X;
    cin >> N >> K >> X;
    vl A(N);
    rep(i, N){
        cin >> A[i];
    }

    sort(all(A));
    reverse(all(A));
    
    // 1 週目
    ll cnt;
    rep(i, N){
        cnt = A[i] / X;
        if(K > cnt){
            K -= cnt;
            A[i] -= cnt * X;
        }else{
            A[i] -= K * X;
            K = 0;
            break;
        }
    }

    sort(all(A));
    reverse(all(A));

    // 2週目
    ll ans = 0;
    rep(i, N){
        if(K > 0){
            K--;
            continue;
        }else{
            ans += A[i];
        }
    }
    cout << ans << endl;
}