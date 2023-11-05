// 宣言
// 1 次元
vector<int> v;
vector<int> v(N);
// 2 次元
vector<vector<mint>> dp(len(i), vector<mint>(len(j), 初期値));
// 3 次元
vector<vector<vector<mint>>> dp(len(i), vector<vector<mint>>(len(j), vector<mint>(len(k), 初期値)));

// 後ろに追加
v.push_back(x);
// 後ろを削除
v.pop_back(x);
// 要素数の変更
v.resize(N, x);

// 比較関数
// 二次元リストを 0 番目をもとに降順ソート, 1 番目は昇順ソート
auto compare=[&](vl &a, vl &b) {
    if(a[0] == b[0]){
        return a[1] < b[1];
    }else{
        return a[0] > b[0];
    }
};
sort(all(ans), compare);

// 二次元リストを 0 番目をもとに昇順ソート, 1 番目は降順ソート
auto compare = [&](vl &a, vl &b) {
    if(a[0] == b[0]){
        return a[1] > b[1];
    }else{
        return a[0] < b[0];
    }
};
sort(all(ans), compare);