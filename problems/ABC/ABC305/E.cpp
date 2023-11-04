#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define rep(i, a, b) for(int i = a; i < b; i++)
#define rrep(i, a, b) for(int i = a; i >= b; i--)
#define fore(i, a) for(auto &i : a)

#define all(x) (x).begin(),(x).end()

int main(){
    int N, M, K;
    cin >> N >> M >> K;
    vector<vector<int>> G(N);
    rep(i, 0, M){
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        G[a].push_back(b);
        G[b].push_back(a);
    }
    priority_queue<pair<int, int>> pq;
    vector<int> HP(N, -1);
    rep(i, 0, K){
        int p, h;
        cin >> p >> h;
        p--;
        pq.push(make_pair(h, p));
        HP[p] = h;
    }
    while(!pq.empty()){
        int h = pq.top().first;
        int v = pq.top().second;
        pq.pop();
        if(HP[v] == h){
            for(int u : G[v]){
                if(HP[u] < h - 1){
                    HP[u] = h - 1;
                    if(h - 1 > 0){
                        pq.push(make_pair(h - 1, u));
                    }
                }
            }
        }
    }
    int cnt = 0;
    vector<int> ans;
    rep(i, 0, N){
        if(HP[i] != -1){
            cnt++;
            ans.push_back(i + 1);
        }
    }
    cout << cnt << endl;
    rep(i, 0, ans.size()){
        cout << ans[i] << " ";
    }
    cout << endl;
}