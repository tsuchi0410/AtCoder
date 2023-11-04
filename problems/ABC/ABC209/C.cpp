#include <bits/stdc++.h>
using namespace std;

int main(){
    
    int N;
    long long MOD = pow(10, 9) + 7;
    cin >> N;
    vector<int> C(N);
    for (int i = 0; i < N; i++){
        cin >> C.at(i);
    }

    sort(C.begin(), C.end());

    long long ans, cnt;
    ans = 1;
    cnt = 0;

    for(int i = 0; i < N; i++){
        ans = ans * (C.at(i) - cnt);
        ans %= MOD;
        cnt++;
    }

    cout << ans << endl;
}