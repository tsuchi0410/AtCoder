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
      rep(l, start, end){
        ll ny = i + dy[k] * l;
        ll nx = j + dx[k] * l;
        if(ny < 0 or H <= ny or nx < 0 or W <= nx){
          break;
        }

        // 処理

      }
    }
  }
}