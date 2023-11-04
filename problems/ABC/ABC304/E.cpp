#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define rep(i, a, b) for(int i = a; i < b; i++)
#define rrep(i, a, b) for(int i = a; i >= b; i--)
#define fore(i, a) for(auto &i : a)

#define all(x) (x).begin(),(x).end()

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
	int size() {
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
    unionfind uf(N);
    int u, v;
    rep(i, 0, M){
        cin >> u >> v;
        u--;
        v--;
        uf.unite(u, v);
    }

    int K;
    cin >> K;
    int x, y;
    set<pair<int, int>> st;
    rep(i, 0, K){
        cin >> x >> y;
        x--;
        y--;
        u = uf.root(x);
        v = uf.root(y);
        if (v < u){
            swap(u, v);
        }
        st.insert(make_pair(u, v));
    }

    int Q;
    cin >> Q;
    int p, q;
    rep(i, 0, Q){
        cin >> p >> q;
        p--;
        q--;
        u = uf.root(p);
        v = uf.root(q);
        if (v < u){
            swap(u, v);
        }
        if (st.count(make_pair(u, v))) {
            cout << "No" << endl;
        } else {
            cout << "Yes" << endl;
        }
    }
}