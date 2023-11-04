// 初期化 O(n);
dsu uf(N);

// 結合 O(α(n))
uf.merge(u, v);

// 連結か判定 O(α(n)) -> bool 
uf.same(u, v);

// 代表元を返す O(α(n)) -> int 
uf.leader(v);

// サイズ O(α(n)) -> int
uf.size(v);

// 連結成分の情報を返す O(n)
vector<vector<int>> G = uf.groups()
auto G = uf.groups()

