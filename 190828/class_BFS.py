from collections import deque
# --------- BFS - gitlab -------------------
# def BFS(s, G):
#
#     visit = [False] * (V + 1)
#     D = [0] * (V + 1)
#
#     Q = deque()
#     Q.append(s)
#     visit[s] = True
#     print(s, end=" ")
#
#     while Q:
#         v = Q.popleft()
#         for w in G[v]:
#             if not visit[w]:
#                 D[w] = D[v] + 1
#                 visit[w] = True
#                 Q.append(w)
#                 print(w, end=" ")
#     print()
#     return D
#
# import sys
# sys.stdin = open("BFS_input.txt", "r")
#
#
# V, E = map(int, input().split())
# G = [[] for _ in range(V + 1)]
#
# for i in range(E):
#     u, v = map(int, input().split())
#     G[u].append(v)
#     G[v].append(u)
#
#
# D = BFS(1, G)
#
# print(D[1:])

# ----------- BFS - class (방문하면서 큐에 넣기) ---------------------
# def BFS(s): # s=시작점
#     # 큐를 생성, 방문표시
#     Q = []
#     visit = [False] * (V + 1) # 1 ~ V까지
#     # 시작점을 방문하고 큐에 삽입
#     visit[s] = True
#     Q.append(s)
#     # 빈큐가 아닐동안
#     while Q:
#         # 큐에서 하나 꺼내온다. v
#         v = Q.pop(0)
#         # print(v)
#         for w in G[v]:
#             # v에 방문하지 않은 인접정점을 모두 찾아서
#             if not visit[w]:
#                 # 차례로 방문하고 큐에 삽입
#                 visit[w] = True
#                 print(w)
#                 Q.append(w)
# import sys
# sys.stdin = open("BFS_input.txt", "r")
#
#
# V, E = map(int, input().split())
# G = [[] for _ in range(V + 1)]
#
# for i in range(E):
#     u, v = map(int, input().split())
#     G[u].append(v)
#     G[v].append(u)
#
# BFS(1)

# ----------- BFS - 최단 경로 ---------------------
def BFS(s): # s=시작점
    # 큐를 생성, 방문표시
    Q = []
    visit = [False] * (V + 1) # 1 ~ V까지
    # 시작점을 방문하고 큐에 삽입
    visit[s] = True
    print(s)
    D[s], P[s] = 0, s
    Q.append(s)
    # 빈큐가 아닐동안
    while Q:
        # 큐에서 하나 꺼내온다. v
        v = Q.pop(0)
        for w in G[v]:
            # v에 방문하지 않은 인접정점을 모두 찾아서
            if not visit[w]:
                # 차례로 방문하고 큐에 삽입
                visit[w] = True; print(w)
                D[w] = D[v] + 1
                P[w] = v
                Q.append(w)
import sys
sys.stdin = open("BFS_input.txt", "r")

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
D = [0] * (V + 1) # 최단거리를 저장
P = [0] * (V + 1) # 최단경로트리

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

BFS(1)
print(D)
print(P)
