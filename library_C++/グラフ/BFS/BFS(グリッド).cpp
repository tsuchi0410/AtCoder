// https://algo-method.com/tasks/424

vl dx = {0, 0, 1, -1};
vl dy = {1, -1, 0, 0};

int main(){
    LL(H, W);
    LL(sh, sw, gh, gw);
    VEC(string, S, H);

    vvl d(H, vl(W, -1));
    d[sh][sw] = 0;
    queue<vl> q;
    q.push({sh, sw});
    while(len(q)){
        ll y = q.front()[0];
        ll x = q.front()[1];
        q.pop();
        // ゴールしたら終わり
        if((y == gh) and (x == gw)){
            break;
        }
        rep(i, len(dx)){
            ll ny = y + dy[i];
            ll nx = x + dx[i];
            if((ny < 0) or (nx < 0) or (ny >= H) or (nx >= W)){
                continue;
            }
            if((d[ny][nx] == -1) and (S[ny][nx] == '.')){
                q.push({ny, nx});
                d[ny][nx] = d[y][x] + 1;
            }
        }
    }
}
