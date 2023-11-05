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
for (auto &p : mp){
    auto key = p.first;
    auto value = p.second;
}