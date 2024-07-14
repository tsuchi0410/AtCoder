// 宣言
// 2 次元
vector<vector<ll>> v;
vector v(j, vector<ll>(i));

// 3 次元
vector<vector<vector<ll>>> v;
vector v(k, vector(j, vector<ll>(i)));

// 後ろに追加
v.push_back(x);
// 後ろを削除
v.pop_back(x);
// 要素数の変更
v.resize(N, x);
// num 番目 の後ろに X を挿入
v.insert(v.begin() + num, X);
// num 番目を削除
v.erase(v.begin() + num);

// 昇順ソート
sort(v.begin(), v,end());
// idx 番目のインデックスで昇順ソート
template<class T, class U>
auto index_sort(vector<T>& v, U idx){
  return stable_sort(v.begin(), v.end(), [&](const vector<long long> &_a_, const vector<long long> &_b_){return _a_[idx] < _b_[idx];});
}
// 降順ソート
template<class T> 
auto rsort(vector<T>& v){ return stable_sort(v.rbegin(), v.rend()); }
// idx 番目のインデックスで降順ソート
template<class T, class U>
auto rsort(vector<T>& v, U idx){
  return stable_sort(v.rbegin(), v.rend(), [&](const vector<long long> &_a_, const vector<long long> &_b_){return _a_[idx] < _b_[idx];});
}

// 反転
reverse(v.begin(), v.end());

// 重複削除
#define unique(v) sort(v.begin(), v.end()), v.erase(unique(v.begin(), v.end()), v.end()), v.shrink_to_fit()

// 最小値
*min_element(v.begin(), v.end());
// 最大値
*max_element(v.begin(), v.end());

// 最小値を更新
template<typename T> void chmin(T& a, T b) { a = min(a, b); }
// 最大値を更新
template<typename T> void chmax(T& a, T b) { a = max(a, b); }

// 二分探索
template <typename T> ll bisect_left(vector<T> &X, ll v){ return lower_bound(X.begin(), X.end(), (ll)v) - X.begin(); }
template <typename T> ll bisect_right(vector<T> &X, ll v){ return upper_bound(X.begin(), X.end(), (ll)v) - X.begin(); }

// 合計
accumulate(v.begin(), v.end(), 0LL);

// 累積和
template <typename T>
vector<T> cumsum(vector<T> &v){
  vector<T> s = {0};
  for(ll i = 0; i < (ll)v.size(); i++) s.push_back(s[i] + v[i]);
  return s;
}

// 比較関数
// 二次元リストを 0 番目をもとに降順ソート, 1 番目は昇順ソート
auto compare=[&](vector<ll> &a, vector<ll> &b) {
    if(a[0] == b[0]){
        return a[1] < b[1];
    }else{
        return a[0] > b[0];
    }
};
sort(all(ans), compare);

// 二次元リストを 0 番目をもとに昇順ソート, 1 番目は降順ソート
auto compare = [&](vector<ll> &a, vector<ll> &b) {
    if(a[0] == b[0]){
        return a[1] > b[1];
    }else{
        return a[0] < b[0];
    }
};
sort(all(ans), compare);