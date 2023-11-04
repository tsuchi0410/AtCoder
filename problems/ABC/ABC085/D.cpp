#include <bits/stdc++.h>
using namespace std;
int main(){
    int N;
    long long H;
    cin >> N >> H;
    long long a, b;
    long long top_a = 0;
    vector<int> L;
    for (int i = 0; i < N; i++) {
        cin >> a >> b;
        top_a = max(top_a, a);
        L.push_back(b);
    }
    sort(L.begin(), L.end());
    reverse(L.begin(), L.end());
    int ans = 0;
    for (long long bi : L) {
        if (bi >= top_a) {
            H -= bi;
            ans++;
        }
        if (H <= 0) {
            break;
        }
    }
    if (H > 0) {
        if (H % top_a == 0) {
            ans += H / top_a;
        } else {
            ans += H / top_a + 1;
        }
    }
    cout << ans << endl;
}