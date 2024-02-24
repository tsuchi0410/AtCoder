lambda dfs = [&](auto&& dfs, vector<vector<ll>> teams, ll np) -> void {
  // 判定 
  if(np == N){
    debug(teams)
    return ;
  }
  
  // 既存のチームに追加
  fore(team, teams){
    team.push_back(np);
    dfs(teams, np + 1);
    team.pop_back();
  }

  // 新規チーム
  teams.push_back({np});
  dfs(teams, np + 1);
  return ;
};
vector<vector<ll>> teams;
dfs(teams, 0);
