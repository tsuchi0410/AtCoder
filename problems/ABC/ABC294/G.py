class SegmentTree:
    def __init__(self, lst, op, e):
        self.n = len(lst)
        self.N = 1 << ((self.n - 1).bit_length())
        self.op = op # operation
        self.e = e # identity element
        self.v = self._build(lst) # self.v is set to be 1-indexed for simplicity
        
    def _build(self, lst):
        # construction of a tree
        # total 2 * self.N elements (tree[0] is not used)
        tree = [self.e] * (self.N) + lst + [self.e] * (self.N - self.n)
        for i in range(self.N - 1, 0, -1): tree[i] = self.op(tree[i << 1], tree[(i << 1)|1])
        return tree
    
    def __getitem__(self, i):
        return self.v[i + self.N]
    
    # update a_i to be x 
    def update(self, i, x):
        v, op = self.v, self.op
        i += self.N
        v[i] = x
        while i > 0:
            i >>= 1 # move to parent
            v[i] = op(v[i << 1], v[(i << 1)|1])
    
    # returns answer for the query interval [l, r)
    def fold(self, l, r):
        N, e, v, op = self.N, self.e, self.v, self.op
        left = l + N; right = r + N
        L = R = e
        while left < right:
            if left & 1: # self.v[left] is the right child
                L = op(L, v[left])
                left += 1
            if right & 1: # self.v[right-1] is the left child
                right -= 1
                R = op(v[right], R)
            left >>= 1; right >>= 1
        return op(L, R)

class LCA:
    def __init__(self, N):
        self.N = N # #vertices
        self.E = [[] for _ in range(N)]
    
    def add_edge(self, init, end, weight, undirected=True):
        self.E[init].append((end, weight))
        if undirected: self.E[end].append((init, weight))
    
    def lca_initialize(self):
        self._eulerian_tour()
        self.sg = SegmentTree(self.euler_tour, min, (float('inf'),))
    
    def _eulerian_tour(self):
        N, E = self.N, self.E
        self.euler_tour = euler_tour = [] # Eulerian tour from the root (0)
        self.depth = depth = [-1] * N # depth[v]: the depth of the vertex v from the root
        self.dist = dist = [float('inf')] * N # dist[v]: the distance of the vertex v from the root.
        self.first_visit = first_visit = [-1] * N
        stack = [(0, -1, 0, 0)] # (vertex, parent, distance, status)
        d = 0 # current depth
        while stack:
            v, p, l, st = stack.pop()
            euler_tour.append((d, v))
            if st == 0: # visited v for the first time
                depth[v] = d; first_visit[v] = len(euler_tour) - 1; dist[v] = l
                n_children = 0
                for u, w in E[v]:
                    if u == p: continue
                    if n_children == 0:
                        stack += [(v, p, l + w, 2), (u, v, l + w, 0)]
                        n_children += 1
                    else:
                        stack += [(v, p, l + w, 1), (u, v, l + w, 0)]
                        n_children += 1
                if n_children == 0: # v is a leaf
                    d -= 1
                else:
                    d += 1
            elif st == 1: # now searching
                d += 1
            else: # search finished
                d -= 1
    
    def lca(self, u, v):
        ui, vi = self.first_visit[u], self.first_visit[v]
        if ui > vi: ui, vi = vi, ui
        return self.sg.fold(ui, vi)[1]
    
    def distance(self, u, v):
        dist = self.dist
        w = self.lca(u, v)
        return dist[u] + dist[v] - 2 * dist[w]

N = int(input())
G = [[] for _ in range(N)]
dic = {}
cnt = []
for i in range(N):
    u, v, w = map(int, input().split())
    if u > v:
        u, v = v, u
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
    dic[(u, v)] = w
    cnt.append((u, v))

dis = LCA()
Q = int(input())
que = []
for i in range(Q):
    num, i, w = map(int, input().split())
    if num == 1:
        dic[cnt[i-1]] = w
    else:
        