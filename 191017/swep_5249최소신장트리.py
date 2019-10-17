import sys
sys.stdin = open('swep_5249_input.txt')

def mstPrim(v):
    D = [11] * (V + 1)
    D[v] = 0
    val = [0] * (V + 1)
    cnt = V + 1

    while cnt:
        u, MIN = 0, 12

        for i in range(V + 1):
            if not visit[i] and MIN > D[i]:
                u, MIN = i, D[i]

        visit[u] = 1

        for v, w in G[u]:
            if not visit[v] and w < D[v]:
                D[v] = w
                # val[v] = w

        cnt -= 1
        print(D)
    return sum(D)

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    visit = [0] * (V + 1)
    for _ in range(E):
        u, v, w = map(int, input().split())
        G[v].append((u, w))
        G[u].append((v, w))

    res = mstPrim(0)

    print('#{} {}'.format(tc, res))