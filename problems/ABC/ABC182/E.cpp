#include <bits/stdc++.h>
using namespace std;
int main(){
    int H, W, N, M;
    cin >> H >> W >> N >> M;
    vector<vector<int>> G(H, vector<int> (W, 0));
    vector<vector<int>> v;
    for (int i = 0; i < N; i++) {
        int A, B;
        cin >> A >> B;
        v.push_back({A - 1, B - 1});
        G[A - 1][B - 1] = 2;
    }
    for (int i = 0; i < M; i++) {
        int C, D;
        cin >> C >> D;
        G[C - 1][D - 1] = -1;
    }
    for (int i = 0; i < N; i++) {
        int A = v[i][0];
        int B = v[i][1];
        G[A][B] = 1;
        // up
        for (int j = A; j >= 0; j--) {
            if (G[j][B] == 0) G[j][B] = 1;
            else if ((G[j][B] == -1) || (G[j][B] == 2)) break;
        }
        // down
        for (int j = A; j < H; j++) {
            if (G[j][B] == 0) G[j][B] = 1;
            else if ((G[j][B] == -1) || (G[j][B] == 2)) break;
        }
        // left
        for (int j = B; j >= 0; j--){
            if (G[A][j] == 0) G[A][j] = 1;
            else if ((G[A][j] == -1) || (G[A][j] == 2)) break;
        }
        // right
        for (int j = B; j < W; j++) {
            if (G[A][j] == 0) G[A][j] = 1;
            else if ((G[A][j] == -1) || (G[A][j] == 2)) break;
        }
    }
    int ans = 0;
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (G[i][j] == 1) ans++;
        }
    }
    cout << ans << endl;
}