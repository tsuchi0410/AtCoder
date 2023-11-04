"""
最小全域木：全域木を構成する辺のコストの総和が最小となるもの
計算量 : O(ElogE + V)

最小全域木問題は、与えられたグラフの最小全域木またはそのコストを求める問題

クラスカル法
グラフの辺をコストが小さい順に閉路を作らないように採用していく

"""

int main(){
    LL(N, M);
    vvl E;
    rep(i, M){
        LL(u, v, w);
        u--;
        v--;
        E.pb({w, u, v});
    }

    sort(E.begin(), E.end());
    
    dsu uf(N);
    ll ans = 0;
    rep(i, M){
        ll w = E[i][0];
        ll u = E[i][1];
        ll v = E[i][2];

        if(uf.same(u, v)){
            continue;
        }

        uf.merge(u, v);
        ans += w;
    }

    print(ans);
}