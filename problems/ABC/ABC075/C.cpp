#include <bits/stdc++.h>
using namespace std;

struct unionfind{
	vector<int> p;
	unionfind(int N){
		p = vector<int>(N, -1);
	}
	int root(int x){
		if (p[x] < 0){
			return x;
		} else {
			p[x] = root(p[x]);
			return p[x];
		}
	}
	bool same(int x, int y){
		return root(x) == root(y);
	}
	void unite(int x, int y){
		x = root(x);
		y = root(y);
		if (x != y){
			if (p[x] < p[y]){
				swap(x, y);
			}
			p[y] += p[x];
			p[x] = y;
		}
	}
    int group_count() {
        int cnt = 0;
        for (int i = 0; i < p.size(); i++) {
            if (p[i] < 0) {
                cnt++;
            }
        }
        return cnt;
    }
};

int main(){
    int N, M;
    cin >> N >> M;
    vector<pair<int, int>> G;
    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        G.push_back(make_pair(a, b));
    }
    int ans = 0;
    for (int i = 0; i < M; i++) {
        unionfind UF(N);
        for (int j = 0; j < M; j++) {
            if (i == j) continue;
            int u, v;
            u = G[j].first;
            v = G[j].second;
            UF.unite(u, v);
        }
        if (UF.group_count() >= 2) ans++;
    }
    cout << ans << endl;
}