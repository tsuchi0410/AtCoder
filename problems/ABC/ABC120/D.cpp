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

int main() {
    int N, M;
    vector<pair<int, int>> V;
    for (int i = 0; i < N; i++) {
        int A, B;
        cin >> A >> B;
        A--;
        B--;
        V.push_back(make_pair(A, B));
    }
    
    reverse(V.begin(), V.end());
    unionfind UF(N);
    vector<long long> ans(M);
    ans[0] = N * (N - 1) / 2;
    
}