/*

木DP
根から最も遠い点までの距離を求める

対応する二項演算：merge
dp[parent]の演算：add_root

dfs で葉まで到達したあと、親に距離を伝播

*/

int main(){
    LL(N);
    vvl G(N);
    rep(i, N - 1){
        LL(u, v);
        G[u].pb(v);
        G[v].pb(u);
    }

    vl cnt(N);
    vl dp(N, -1);
    ll root = 0;
    lambda merge = [&](auto&& merge, ll dp_cum, ll dist) -> ll {
        return max(dp_cum, dist);
    };

    lambda add_root = [&](auto&& add_root, ll dist) -> ll {
        return dist + 1;
    };

    lambda dfs = [&](auto&& dfs, ll v, ll p) -> void {
        // 末端に到達したら return
        if(G[v].size() == 1){
            dp[v] = 0;
            return;
        }

        ll dp_cum = 0;
        fore(nv, G[v]){
            // p : 親, nv : 子, 親 -> 子の順で探索
            if(nv == p){
                continue;
            }
            dfs(nv, v);
            dp_cum = merge(dp_cum, dp[nv]);
        }

        dp[v] = add_root(dp_cum);
    };

    dfs(root, -1);
}