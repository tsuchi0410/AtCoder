#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    string S1, S2, S3;
    cin >> S1 >> S2 >> S3;
    int N1 = S1.length();
    int N2 = S2.length();
    int N3 = S3.length();

    unordered_set<char> S;
    for (char c : S1)
        S.insert(c);
    for (char c : S2)
        S.insert(c);
    for (char c : S3)
        S.insert(c);

    if (S.size() > 10) {
        cout << "UNSOLVABLE" << endl;
        return 0;
    }

    vector<char> chars(S.begin(), S.end());
    vector<int> digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    vector<int> indices(chars.size());
    iota(indices.begin(), indices.end(), 0);

    bool foundSolution = false;
    do {
        vector<int> mapping(26, -1);
        bool isValidMapping = true;
        for (int i = 0; i < chars.size(); i++) {
            mapping[chars[i] - 'A'] = digits[indices[i]];
            if (i < 10 && mapping[chars[i] - 'A'] == 0) {
                isValidMapping = false;
                break;
            }
        }

        if (!isValidMapping)
            continue;

        long long num1 = 0, num2 = 0, num3 = 0;
        for (char c : S1)
            num1 = num1 * 10 + mapping[c - 'A'];
        for (char c : S2)
            num2 = num2 * 10 + mapping[c - 'A'];
        for (char c : S3)
            num3 = num3 * 10 + mapping[c - 'A'];

        if (N1 != to_string(num1).length() || N2 != to_string(num2).length() || N3 != to_string(num3).length())
            continue;
        if (num1 == 0 || num2 == 0 || num3 == 0)
            continue;
        if (num1 + num2 == num3) {
            cout << num1 << endl;
            cout << num2 << endl;
            cout << num3 << endl;
            foundSolution = true;
            break;
        }
    } while (next_permutation(indices.begin(), indices.end()));

    if (!foundSolution)
        cout << "UNSOLVABLE" << endl;

    return 0;
}
