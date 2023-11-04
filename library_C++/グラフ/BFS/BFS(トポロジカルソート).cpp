/*
https://algo-method.com/tasks/964

トポロジカルソート
計算量 : O(V + E)
概要 :
入次数をカウント
入次数が 0 の頂点を q に追加
while(len(q)){
    1. キューから取り出した次数が 0 の点をトポロジカルソートした時の次の頂点として採用し、その頂点をグラフから削除する
    2. 新たに次数が 0 になったところをキューに入れる
}

※ 閉路がない有向辺のときしかできない
*/

int main(){
    LL(N, M);
    vvl G(N);
    rep(i, M){
        LL(v, u);
        G[v].pb(u);
    }

    vl order;  // トポロジカルソートの結果を格納

    vl ind(N);  // indegree : 入次数
    rep(v, N){
        fore(u, G[v]){
            ind[u]++;
        }
    }

    queue<ll> q;
    // 入次数 = 0 の頂点から探索
    rep(v, N){
        if(ind[v] == 0){
            q.push(v);
        }
    }
    while(len(q)){
        ll v = q.front();
        q.pop();

        order.pb(v);  // トポロジカルソートの結果を追加

        fore(nv, G[v]){
            ind[nv]--;  // v -> nv から、v を削除するので入次数を 1 減らす
            if(ind[nv] == 0){
                q.push(nv);
            }
        }
    }

    fore(v, order) cout << v << " ";
    cout << endl;
}