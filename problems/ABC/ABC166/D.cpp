#include <bits/stdc++.h>
using namespace std;
int main(){
    long long X;
    cin >> X;
    for (int A = -1000; A < 1000; A++) {
        for (int B = -1000; B < 1000; B++) {
            if (pow(A, 5) - pow(B, 5) == X) {
                cout << A << " " << B << endl;
                return 0;
            }
        }
    }
}