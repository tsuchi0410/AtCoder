// 縦横
vector<ll> dx = {0, 0, 1, -1};
vector<ll> dy = {1, -1, 0, 0};

// 斜め
vector<ll> dx = {1, 1, -1, -1};
vector<ll> dy = {1, -1, -1, 1};

// 縦横斜め
vector<ll> dx = {-1, 1, 0, 0, 1, 1, -1, -1};
vector<ll> dy = {0, 0, -1, 1, 1, -1, -1, 1};

// 六角形グリッド
vector<ll> dx = {-1, -1, 0, 0, 1, 1};
vector<ll> dy = {-1, 0, -1, 1, 0, 1};

// 境界チェック例
rep(i, H){
  rep(j, W){
    rep(k, len(dx)){
      if(i + dy[k] * 上限 < 0 or H <= i + dy[k] * 上限){
        continue;
      }
      if(j + dx[k] * 上限 < 0 or W <= j + dx[k] * 上限){
        continue;
      }
      rep(l, 上限 + 1){
        ll ny = i + dy[k] * l;
        ll nx = j + dx[k] * l;
      }
    }
  }
}