#include <bits/stdc++.h>
using namespace std;
int main(){
    int N;
    cin >> N;
    string S;
    cin >> S;
    unordered_map<char, unordered_set<int>> mp;
    for (int i = 0; i < S.size(); i++) {
        if (S[i] == 'R') mp['R'].insert(i);
        if (S[i] == 'G') mp['G'].insert(i);
        if (S[i] == 'B') mp['B'].insert(i);
    }
    for (int i = 0; i < mp['R'].size(); i++) {
        for (int j = 0; j < mp['G'].size(); j++) {
            

        }
    }
}