import sys
sys.stdin = open('swep_5248_input.txt')

from collections import deque

def bfs(n):
    Q=deque()
    Q.append(n)

    while Q:
        v = Q.popleft()
        for w in G[v]:
            if visit[w] == 1:
                visit[w] = 0
                bfs(w)
            else:
                pass


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    G = [[0] for _ in range(N + 1)]
    visit = [0] * (N + 1)

    for i in range(0, M * 2 - 1, 2):
        G[arr[i]].append(arr[i + 1])
        G[arr[i + 1]].append(arr[i])
        visit[arr[i]] = visit[arr[i + 1]] = 1
    cnt = visit.count(0) - 1
    for i in range(N + 1):
        if visit[i] == 1:
            bfs(i)
            cnt += 1
    print('#{} {}'.format(tc, cnt))
