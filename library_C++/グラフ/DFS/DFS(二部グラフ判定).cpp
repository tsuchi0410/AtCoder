/*
https://algo-method.com/tasks/961

計算量 : O(V + E)
概要 :
二部グラフかを判定する
vl color を追加する（白 = 0, 黒 = 1, 未探索 = -1）
始点を 0 として、塗り分けを行う

*/

int main(){
    LL(N, M);
    vvl G(N);
    rep(i, M){
        LL(v, u);
        v--;
        u--;
        G[v].pb(u);
        G[u].pb(v);
    }

    vl color(N, -1);
    bool isnibu = true;
    lambda dfs = [&](auto&& dfs, ll v) -> void {
        fore(nv, G[v]){
            if(color[nv] != -1){
                if(color[v] == color[nv]){
                    isnibu = false;
                }
                continue;
            }
            color[nv] = 1 ^ color[v];
            dfs(nv);
        }
        return;
    };

    rep(v, N){
        if(color[v] != -1){
            continue;
        }
        color[v] = 0;
        dfs(v);
    }

    if(isnibu){
        print("Yes");
    }else{
        print("No");
    }
}