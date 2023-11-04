/*
https://algo-method.com/tasks/963/editorial

トポロジカルソート
計算量 : O(V + E)
概要 :
dfs の帰りがけ時に頂点を追加していく
最後に反転する

※ 閉路がない有向辺のときしかできない

*/

int main(){
    LL(N, M);
    vvl G(N);
    rep(i, M){
        LL(v, u);
        v--;
        u--;
        G[v].pb(u);
    }

    vl order;  // トポロジカルソートの結果を格納

    vector<bool> seen(N, false);
    lambda dfs = [&](auto&& dfs, ll v) -> void {
        seen[v] = true;
        fore(nv, G[v]){
            if(seen[nv] == true){
                continue;
            }
            dfs(nv);
        }
        // 帰りがけに頂点を追加
        order.pb(v);
        return;
    };

    rep(v, N){
        if(seen[v] == true){
            continue;
        }
        dfs(v);
    }

    rev(order);
    fore(v, order) cout << v << " ";
    cout << endl;    
}