/*
https://algo-method.com/tasks/968

計算量 : O(V + E)
概要 :
s - t パス（有向辺）
通常の BFS に、どこから来たかをもつ prev 配列を追加

*/


int main(){
    LL(N, M, s, t);
    vvl G(N);
    rep(i, M){
        LL(v, u);
        v--;
        u--;
        G[v].push_back(u);
    }

    vector<bool> seen(N, false);
    vl prev(N, -1);
    queue<ll> q;
    q.push(s);
    seen[s] = true;
    while(len(q)){
        ll v = q.front();
        q.pop();
        fore(nv, G[v]){
            if(seen[nv] == true){
                continue;
            }
            seen[nv] = true;
            prev[nv] = v;
            q.push(nv);
        }
    }

    vl path;
    ll pos = t;
    while(pos != -1){
        path.push_back(pos);
        pos = prev[pos];
    }

    rev(path);

    print(len(path));
    fore(v, path) cout << v << " ";
    cout << endl;
    
}