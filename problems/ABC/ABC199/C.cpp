#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int N; string S; int Q;

int main(){
    
    cin >> N >> S >> Q;
    string S2 = S.substr(0,N)+S.substr(N);

    int cnt = 0;

    for(int i = 1; i <= Q; i++){
        
        int T, A, B;
        cin >> T >> A >> B;
        A--; B--;

        if (cnt % 2 == 0 && T == 1){
            swap(S[A],S[B]);
            swap(S2[(A+10*N)%N],S2[(B+10*N)%N]);
        }

        if (cnt % 2 == 1 && T == 1){
            swap(S2[A],S2[B]);
            swap(S[(A+10*N)%N],S[(B+10*N)%N]);
        }

        if (T == 2){
            cnt++;
        }
        
        
    }

    if (cnt % 2 == 0){
        cout << S << endl;
    }else{
        cout << S << endl;
    }

}