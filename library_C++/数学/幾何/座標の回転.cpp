"""
ラジアン = 度 * (PI / 180)
cout << fixed << setprecision(10);
d = d * (PI / 180);
auto p = rotate(a, b, d);

"""


"""
原点周りで反時計回りに radian 回転

"""

pair<ld, ld> rotate(ld x, ld y, ld radian){
    ld nx = x * cos(radian) - y * sin(radian);
    ld ny = x * sin(radian) + y * cos(radian);
    return mp(nx, ny);
}
