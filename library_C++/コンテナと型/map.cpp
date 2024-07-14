// 宣言
map<int, int> mp;
unordered_map<int, int> ump; // pair や tuple などは key にできない

// 追加
mp[1] = 10;
// 削除
mp.erase(1);

// アクセス
mp.at(1)
// 最初 / 最後 の要素にアクセス
auto [k, v] = *mp.begin();
auto [k, v] = *--mp.end();

// 所属判定
mp.contains(x)
// 要素数
mp.size()

// ループ
  for(auto &[k, v] : mp){
  }

// vector の要素数をカウント
// unordered_map<ll, ll> mp = counter(v);
template <typename T>
unordered_map<T, ll> counter(vector<T> &v){
  unordered_map<T, ll> mp;
  for(ll i = 0; i < (ll)v.size(); i++) mp[v[i]]++;
  return mp;
}
// map<ll, ll> mp = counter(v);
template <typename T>
map<T, ll> counter(vector<T> &v){
  map<T, ll> mp;
  for(ll i = 0; i < (ll)v.size(); i++) mp[v[i]]++;
  return mp;
}
// string の要素数をカウント
// unordered_map<char, ll> mp = counter(s);
unordered_map<char, ll> counter(string &v){
  unordered_map<char, ll> mp;
  for(ll i = 0; i < (ll)v.size(); i++) mp[v[i]]++;
  return mp;
}
// map<char, ll> mp = counter(s);
map<char, ll> counter(string &v){
  map<char, ll> mp;
  for(ll i = 0; i < (ll)v.size(); i++) mp[v[i]]++;
  return mp;
}