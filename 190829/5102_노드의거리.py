import sys
sys.stdin = open('5102_input.txt', 'r')

def BFS(s, f):
    Q = []
    Q.append(s)
    visit[s] = 1
    print(visit)
    D[s] = 0
    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if not visit[w]:
                visit[w] = 1
                D[w] = D[v] + 1
                if w == f:
                    return D[w]
                Q.append(w)
    return 0
for t in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    visit = [0] * (V + 1)
    D = [0] * (V + 1)
    for _ in range(E):
        u, V = map(int, input().split())
        G[u].append(V)
        G[V].append(u)
    S, F = map(int, input().split())
    if S != F:
        res = BFS(S, F)
    else:
        res = 0

    print('#{} {}'. format(t, res))