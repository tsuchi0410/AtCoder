#include <bits/stdc++.h>
using namespace std;
int main(){
    int N, M;
    cin >> N >> M;
    unordered_map<int, int> ump;
    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        if (a < b) ump[b]++;
        else if (b < a) ump[a]++;
    }
    int ans = 0;
    for (auto &p : ump) {
        auto k = p.first;
        auto v = p.second;
        if (v == 1) ans++;
    }
    cout << ans << endl;
}