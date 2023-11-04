/*
右シフトビット 1/2
6 -> 3
110 -> 011
*/

#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main(){
    ll N;
    cin >> N;
    cout << (N >> 1LL) << endl;
}