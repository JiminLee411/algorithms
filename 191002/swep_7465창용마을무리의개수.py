import sys

sys.stdin = open('swep_7465_input.txt', 'r')

import collections

def BFS(v):
    Q.append(v)
    visit[v] = 1
    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visit[w]:
                Q.append(w)
                visit[w] = 1
    return 1



for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    visit = [0] * (N + 1)
    cnt = 0

    for _ in range(M):
        v, u = map(int, input().split())
        G[v].append(u)
        G[u].append(v)

    Q = collections.deque()
    for i in range(1, N + 1):
        if not visit[i]:
            cnt += BFS(i)

    print('#{} {}'. format(tc, cnt))