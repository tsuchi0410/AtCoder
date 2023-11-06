/*

d = マンハッタン距離とすると、

d = |xi - xj| + |yi - yj|
  = max(xi - xj, xj - xi) + max(yi - yj, yj - yi)

2 * 2 で 4 通りあるので、

(中略)

d = max( xi + yi - xj - yj,
         xi - yi - xj + yj,
        -xi + yi + xj - yj,
        -xi - yi + xj + yj)

*/