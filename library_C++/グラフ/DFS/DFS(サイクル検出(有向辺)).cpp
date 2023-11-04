// https://algo-method.com/tasks/970

int main(){
  LL(N, M);
  vvl G(N);
  rep(i, M){
    LL(u, v);
    u--;
    v--;
    G[u].push_back(v);
  }

  vector<bool> seen(N, false);
  vector<bool> finished(N, false);
  lambda dfs = [&](auto &&dfs, ll v) -> bool{
    bool iscycle = false;
    seen[v] = true;
    fore(nv, G[v]){
      if (seen[nv] == true){
        if (finished[nv] == false)
        { // 行きがけ順のときに未探索な帰りがけの頂点を見つけた
          return true;
        }
        continue;
      }
      iscycle |= dfs(nv);
    }
    // 帰りがけ
    finished[v] = true;
    return iscycle;
  };

  rep(v, N){
    if (seen[v] == true){
      continue;
    }
    bool iscycle = dfs(v);
    if (iscycle == true){
      print("Yes");
      return 0;
    }
  }
  print("No");
}