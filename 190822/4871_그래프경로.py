import sys

sys.stdin = open('4871_input.txt', 'r')

def DFS(v, G):
    stack = []
    stack.append(v)
    visit[v] = True

    for w in graph[v]:
        if w == G:
            return 1
        if not visit[w]:
            if DFS(w, G) == 1:
                return 1
    return 0

for t in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visit = [False] * (V + 1)

    for _ in range(E):
        departure, arrival = map(int, input().split())
        graph[departure].append(arrival)
    S, G = map(int, input().split())

    res = DFS(S, G)

    print('#{} {}'. format(t, res))