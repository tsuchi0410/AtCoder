#include <bits/stdc++.h>
using namespace std;
long long INF = powl(10, 18);
int main(){
    long long N, M;
    cin >> N >> M;
    long long ans = INF;
    int cnt = 0;
    long long b;
    for (long long a = 1; a < INF; a++) {
        b = (M + cnt) / a;
        if (a > b) break;
        if ((b <= N) && (a * b >= M)) ans = min(ans, a * b);
        cnt++;
    }
    if (ans == INF) ans = -1;
    cout << ans << endl;
}