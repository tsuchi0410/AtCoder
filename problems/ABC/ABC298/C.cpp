#include <bits/stdc++.h>
using namespace std;
int main(){
    int N, Q;
    cin >> N >> Q;
    unordered_map<int, multiset<int>> mp1;
    unordered_map<int, set<int>> mp2;
    for (int ii = 0; ii < Q; ii++){
        int op;
        cin >> op;
        if (op == 1){
            int i, j;
            cin >> i >> j;
            mp1[j].insert(i);
            mp2[i].insert(j);
        }
        if (op == 2){
            int i;
            cin >> i;
            for (auto &x : mp1[i]){
                cout << x << " ";
            }
            cout << endl;
        }
        if (op == 3){
            int i;
            cin >> i;
            for (auto &x : mp2[i]){
                cout << x << " ";
            }
            cout << endl;
        }

    }
}
