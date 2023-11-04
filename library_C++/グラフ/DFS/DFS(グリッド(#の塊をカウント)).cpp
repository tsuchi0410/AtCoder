// https://algo-method.com/tasks/955

vl dx = {0, 0, 1, -1};
vl dy = {1, -1, 0, 0};

int main(){
    LL(H, W);
    VEC(string, S, H);
    vector<vector<bool>> seen(H, vector<bool>(W, false));
    lambda dfs = [&](auto&& dfs, ll y, ll x) -> void {
        seen[y][x] = true;
        rep(i, len(dx)){
            ll ny = y + dy[i];
            ll nx = x + dx[i];
            if((ny < 0) or (nx < 0) or (ny >= H) or (nx >= W)){
                continue;
            }
            if((seen[ny][nx] == false and S[ny][nx] == '#')){
                dfs(ny, nx);
            }
        }
        return;
    };

    ll cnt = 0;
    rep(i, H){
        rep(j, W){
            if(seen[i][j] == false and S[i][j] == '#'){
                dfs(i, j);
                cnt++;
            }
        }
    }

    print(cnt);
}
