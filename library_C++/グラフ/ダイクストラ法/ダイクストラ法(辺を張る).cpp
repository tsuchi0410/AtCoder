/*

varified
https://atcoder.jp/contests/abc213/tasks/abc213_e

概要 : 
隣接する辺にコスト 0 、2 * 2 の壁を破壊するときにコスト 1 の辺を張る
flatten 関数を使う

*/

vl dx = {0, 0, 1, -1};
vl dy = {1, -1, 0, 0};

ll flatten(ll H, ll i, ll j){
    return i + H * j;
}

vector<ll> unflatten(ll H, ll val){
    ll y = val % H;
    ll x = val / H;
    return {y, x};
}


int main(){
    LL(H, W);
    VEC(string, S, H);

    ll N = H * W;
    vvvl G(N);
    vl dist(N, INF);
    dist[0] = 0;
    vector<bool> seen(N, false);

    // {cost, v}
    pqg<vl> q;
    q.push({0, 0});

    while(len(q)) {
        ll cost_v = q.top()[0];
        ll v = q.top()[1];
        q.pop();
        if(seen[v]) continue;
        seen[v] = true;

        ll y = unflatten(H, v)[0];
        ll x = unflatten(H, v)[1];
        rep(i, len(dx)){
            ll ny = y + dy[i];
            ll nx = x + dx[i];
            if((ny < 0) or (nx < 0) or (ny >= H) or (nx >= W)){
                continue;
            }
            if(S[ny][nx] == '#'){
                continue;
            }
            ll nv = flatten(H, ny, nx);
            ll cost_nv = 0;
            if(dist[nv] > cost_v + cost_nv){
                dist[nv] = cost_v + cost_nv;
                q.push({dist[nv], nv});
            }
        }
        rep(i, -2, 3){
            rep(j, -2, 3){
                if(abs(i) + abs(j) >= 4){
                    continue;
                }
                ll ny = y + i;
                ll nx = x + j;
                if((ny < 0) or (nx < 0) or (ny >= H) or (nx >= W)){
                    continue;
                }
                // debug(i, j)
                ll nv = flatten(H, ny, nx);
                ll cost_nv = 1;
                if(dist[nv] > cost_v + cost_nv){
                    dist[nv] = cost_v + cost_nv;
                    q.push({dist[nv], nv});
                }
            }
        }
    }

    debug(dist)
    print(dist[H * W - 1]);
}