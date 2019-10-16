from collections import deque

def BFS(s):
    D = [0xfffffff] * (V + 1)   # D[] 초기값을 아주 큰 값으로 설정
    # visit = [False] * (V + 1)
    visit = [False] * (V + 1)   # 이미 최단 경로를 찾은 정점들과 아닌 정점들 구분
    D[s] = 0
    cnt = V # 정점의 갯수만큼만 돌리면 된다.

    while cnt:
        # 아직 선택하지 않은 정점 중에 D[]가 최소인 정점을 찾는다.
        for v, w in G[u]:
            if D[v] > D[u] + w:    # u(현재위치) -----> v(갈 위치)
                D[v] += D[u] + w

V, E = map(int, input().split())    # 정점수, 간선수
G = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))
