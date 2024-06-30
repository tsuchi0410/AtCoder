// 宣言
// 2 次元
vector v(, vector<ll>());
// 3 次元
vector v(, vector(, vector<ll>()));

// 後ろに追加
v.push_back(x);
// 後ろを削除
v.pop_back(x);
// 要素数の変更
v.resize(N, x);

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

// map を vector に使う
vector<unordered_map<string, ll>> v(N + 1);