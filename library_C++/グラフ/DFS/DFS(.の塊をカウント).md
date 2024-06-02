## 問題 . の数をカウント
D - Grid and Magnet
https://atcoder.jp/contests/abc351/tasks/abc351_d
---

S は以下のようにする
.!!#!.
!#!...
.!....

!の周りは、それ以上 DFS できないことを意味する。. の塊の最大数は？

### コード
```cpp
vector<ll> dx = {0, 0, 1, -1};
vector<ll> dy = {1, -1, 0, 0};

int main(){
  LL(H, W);
  VEC(string, S, H);
  vector<vector<bool>> seen(H, vector<bool>(W, false));

  rep(i, H){
    rep(j, W){
      if(S[i][j] == '#'){
        rep(k, len(dx)){
          ll ny = i + dy[k];
          ll nx = j + dx[k];
          if((ny < 0) or (nx < 0) or (ny >= H) or (nx >= W)){
            continue;
          }
          if(S[ny][nx] == '#'){
            continue;
          }
          S[ny][nx] = '!';
        }
      }
    }
  }

  ll ans = 1;
  ll cnt = 0;
  unordered_set<vector<ll>> rec;
  lambda dfs = [&](auto&& dfs, ll y, ll x) -> void {
    if(S[y][x] == '!'){
      rec.insert({y, x});
      return ;
    }
    seen[y][x] = true;
    cnt++;
    rep(i, len(dx)){
      ll ny = y + dy[i];
      ll nx = x + dx[i];
      if((ny < 0) or (nx < 0) or (ny >= H) or (nx >= W)){
        continue;
      }
      if(seen[ny][nx] == false){
        if(S[ny][nx] == '.' or S[ny][nx] == '!'){
        dfs(ny, nx);
        }
      }
    }
    return;
  };

  rep(i, H){
    rep(j, W){
      if(seen[i][j] == false and S[i][j] == '.'){
        dfs(i, j);
        chmax(ans, len(rec) + cnt);
        debug(ans, i, j)
        cnt = 0;
        rec.clear();
      }
    }
  }
  print(ans);
}
```

***