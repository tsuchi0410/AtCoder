#include <bits/stdc++.h>
using namespace std;

int main(){
    int MOD = 10;
    int N;
    cin >> N;
    vector<string> S(N);
    for(int i = 0; i < N; i++){
        cin >> S[i];
    }
    for(int i = 0; i < N; i++){
        cout << int(S[i]) % 10 << endl;
    }

}