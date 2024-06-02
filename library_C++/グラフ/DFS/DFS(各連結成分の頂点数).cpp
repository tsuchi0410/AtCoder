int main(){ 
  LL(N, M);
  vector<vector<ll>> G(N);
  rep(i, M){
    LL(A, B);
    A--;
    B--;
    G[A].push_back(B);
    G[B].push_back(A);
  }

  ll v_cnt = 0; // 各頂点数
  vector<bool> seen(N, false);
  lambda dfs = [&](auto&& dfs, ll v) -> void {
    seen[v] = true;
    v_cnt++; // 頂点数をカウント
    fore(nv, G[v]){
      if(seen[nv] == true){
        continue;
      }
      dfs(nv);
    }
    return;
  };

  rep(v, N){
    if(seen[v] == false){
      dfs(v);
      print(v_cnt);
    }
  }
}