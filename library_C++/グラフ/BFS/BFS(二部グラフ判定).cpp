/*
https://algo-method.com/tasks/962

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
        LL(u, v);
        G[u].pb(v);
        G[v].pb(u);
    }
    
    bool isnibu = true;
    vl color(N, -1);  // color 0, 1, -1
    rep(v, N){
        // 訪問済みであればスキップ
        if(color[v] != -1){
            continue;
        }
        queue<ll> q;
        color[v] = 0;
        q.push(v);
        while(len(q)){
            ll u = q.front();
            q.pop();
            fore(nu, G[u]){
                if(color[nu] != -1){
                    if(color[nu] == color[u]){
                        isnibu = false;
                    }
                    continue;
                }
                color[nu] = 1 ^ color[u];
                q.push(nu);
            }
        }
    }

    if(isnibu == true){
        print("Yes");
    }else{
        print("No");
    }
}