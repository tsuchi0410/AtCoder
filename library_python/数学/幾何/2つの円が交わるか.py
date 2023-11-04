"""
半径 r1 の円 C1 と、半径 r2 の円 C2 が 2 点交わる条件は、
r1 - r2 < d(O1 * O2) < r1 + r2

1点で交わるときも含めたいときは、
r1 - r2 <= d(O1 * O2) <= r1 + r2

誤差が怖いので二乗して判定

"""
def ed(xa, ya, xb, yb):
    return (xa - xb) ** 2 + (ya - yb) ** 2


if abs(R[v] - R[u]) ** 2 < ed(X[v], Y[v], X[u], Y[u]) < (R[v] + R[u]) ** 2:
