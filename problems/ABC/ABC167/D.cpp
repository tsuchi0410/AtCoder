#include <bits/stdc++.h>
using namespace std;
int main(){
    int N;
    long long K;
    cin >> N >> K;
    vector<int> A;
    for (int i = 0; i < N; i++) {
        int a;
        cin >> a;
        A.push_back(a - 1);
    }
    unordered_map<int, int> mp;
    mp[0] = 0;
    int cnt = 1;
    int i = 0;
    pair<int, int> t;
    while (true) {
        if (mp.count(A[i])) {
            t = make_pair(mp.at(A[i]), cnt);
            break;
        } else {
            mp[A[i]] = cnt;
        }
        cnt++;
        i = A.at(i);
    }

    // cout << t.first <<  " " <<  t.second << endl;
    // for (auto item : mp) {
    //     cout << item.first << " " << item.second << endl;
    // }

    if (K <= t.first) {
        for (auto item : mp) {
            if (item.second == K) cout << item.first + 1 << endl;
        }
    } else {
        K -= t.first;
        K %= t.second - t.first;
        for (auto item : mp) {
            if (item.second == t.first + K) cout << item.first + 1 << endl;
        }
    }
}