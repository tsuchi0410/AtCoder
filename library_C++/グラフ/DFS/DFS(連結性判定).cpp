// https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_am

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

    vector<bool> seen(N, false);
    lambda dfs = [&](auto&& dfs, ll v) -> void {
        seen[v] = true;
        fore(nv, G[v]){
            if(seen[nv] == true){
                continue;
            }
            dfs(nv);
        }
        return;
    };

    dfs(0);

    bool f = true;
    rep(i, N){
        if(seen[i] == false) f = false;
    }

    if(f == true){
        print("The graph is connected.");
    }else{
        print("The graph is not connected.");
    }
}