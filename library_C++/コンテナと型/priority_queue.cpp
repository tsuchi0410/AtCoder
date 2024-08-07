// 宣言
priority_queue<ll> pq; // 最も大きいものを取り出す
priority_queue<ll, vector<ll>, greater<ll>> pq; // 小さい順に取り出す

// 追加
pq.push(10);
// 最大の要素を取得
pq.top();
// 最大の要素を削除
pq.pop();
// 要素数の取得
pq.size();