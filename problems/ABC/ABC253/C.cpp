#include <bits/stdc++.h>
using namespace std;
int main(){
    int Q;
    cin >> Q;
    multiset<int> st;
    for (int i = 0; i < Q; i++) {
        int op;
        cin >> op;
        if (op == 1) {
            int x;
            cin >> x;
            st.insert(x);
        }
        if (op == 2) {
            int x, c;
            cin >> x >> c;
            for (int i = 0; i < c; i++) {
                auto itr = st.find(x);
                if (itr != st.end()) {
                    st.erase(itr);
                } else {
                    break;
                }
            }
        }
        if (op == 3) {
            cout << *st.rbegin() - *st.begin() << endl;
        }
    }
}