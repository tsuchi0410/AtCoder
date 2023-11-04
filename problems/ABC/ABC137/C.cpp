#include <bits/stdc++.h>
using namespace std;
int main(){
    int N;
    cin >> N;
    unordered_map<string, int> ump;
    for (int i = 0; i < N; i++) {
        string s;
        cin >> s;
        sort(s.begin(), s.end());
        ump[s]++;
    }
    long long ans = 0;
    for (auto iter = ump.begin(); iter != ump.end(); iter++) {
        long long key = iter->second;
        ans += key * (key - 1) / 2;
    }
    cout << ans << endl;
}