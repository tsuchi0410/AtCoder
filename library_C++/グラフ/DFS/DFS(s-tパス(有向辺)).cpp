/*
https://algo-method.com/tasks/969

計算量 : O(V + E)
概要 :
s - t パス（有向辺）
通常の DFS に、どこから来たかをもつ prev 配列を追加

*/

int main(){
    LL(N, M, s, t);
    vvl G(N);
    rep(i, M){
        LL(v, u);
        v--;
        u--;
        G[v].pb(u);
    }

    vector<bool> seen(N, false);
    vl prev(N, -1);
    lambda dfs = [&](auto&& dfs, ll v) -> void {
        seen[v] = true;
        fore(nv, G[v]){
            if(seen[nv] == true){
                continue;
            }
            prev[nv] = v;  // どこから来たかを記憶
            dfs(nv);
        }
        return;
    };

    dfs(s);

    vl path;
    ll pos = t;
    while(pos != -1){
        path.pb(pos);
        pos = prev[pos];
    }

    rev(path);

    print(len(path));
    fore(v, path) cout << v << " ";
    cout << endl;
}