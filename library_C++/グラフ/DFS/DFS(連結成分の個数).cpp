// https://algo-method.com/tasks/956

int main(){
  LL(N, M);
  vvl G(N);
  rep(i, M){
    LL(v, u);
    v--;
    u--;
    G[v].push_back(u);
    G[u].push_back(v);
  }

  vector<bool> seen(N, false);
  lambda dfs = [&](auto&& dfs, ll v) -> void {
    seen[v] = true;
    fore(nv, G[v]){
      if(seen[nv] == true){
        continue;
      }
      dfs(nv);
    }
    return;
  };

  ll cnt = 0;
  rep(v, N){
    if(seen[v] == false){
      cnt++;
      dfs(v);
    }
  }

  print(cnt);
}