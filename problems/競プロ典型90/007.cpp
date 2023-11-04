#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < n; i++)
#define append push_back

int main(){

    int n;
    cin >> n;

    vector<int> a(n);
    rep(i, n) a[i];
    sort(a.begin(), a.end());

    int q;
    cin >> q;
    
    int b;
    vector<int> b(n);
    for(int i = 0; i < q; i++){
        
        cin >> b;
        auto idx = lower_bound(a.begin(), a.end(), b);

        if(idx == 0){
            cout << abs(b - a.at(idx)) << endl;
        }else if(idx == a.size()){
            cout << abs(b - a.at(idx-1)) << endl;
        }else{
            cout << abs(b - a.at(idx)) << endl;
        }

        }

    }


}