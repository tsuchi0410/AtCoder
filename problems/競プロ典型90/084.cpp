#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    string s;
    cin >> n >> s;
    vector<int> maru, batu;
    for (int i = 0; i < n; i++){
        if (s == "o"){
            maru.push_back(i);
        }else{
            batu.push_back(i);
        }
    }

    for (int i = 0; i < maru.size(); i++){
        cout << maru[i] << endl;       
    }
    


}