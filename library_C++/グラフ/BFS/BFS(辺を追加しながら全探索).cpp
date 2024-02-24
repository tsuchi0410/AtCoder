// 探索する範囲 set, map, vector などで管理
// グリッド状態の全探索は map[grid] = dist とすればよい
vector<ll> d(N, -1);

queue<ll> q;
q.push(0);
d[0] = 0;

while(len(q)){
  ll v = q.front();
  q.pop();
  
  // 何らかの処理

  // 次見る場所を追加

  // 有向辺を繋げながらBFS
  fore(nv, next){
    if(条件 and d[nv] == -1){
      d[nv] = d[v] + 1; // チェック
      q.push(nv);
    }
  }
}