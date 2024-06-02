"""
二次元配列を90度時計回りに回転

vvl data;

auto data2 = rotate2d(data);

data = data2;
"""



vector<vector<ll>> rotate2d(vector<vector<ll>>& matrix) {
    ll n = matrix.size();
    vector<vector<ll>> rotatedMatrix(n, vector<ll>(n, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            rotatedMatrix[j][n - 1 - i] = matrix[i][j];
        }
    }
    return rotatedMatrix;
}