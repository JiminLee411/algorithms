import sys

sys.stdin = open('swep_1953_input.txt', 'r')

from collections import deque

def bfs(x, y, l):
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        point = unders[x][y]
        for dx, dy in direction[point]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not visited[nx][ny] and unders[nx][ny] != 0 and (-1*dx, -1*dy) in direction[unders[nx][ny]]:
                visited[nx][ny] = visited[x][y] + 1
                if visited[nx][ny] <= L:
                    cnt += 1
                    q.append((nx, ny))
    from pprint import pprint
    pprint(visited,width=M*10)
    return cnt



T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    unders = [list(map(int, input().split())) for _ in range(N)]
    # 1 : 상하좌우, 2 : 상하, 3 : 좌우, 4 : 상우, 5 : 하우, 6 : 좌하, 7 : 좌상
    direction = {0: [], 1: ((0, 1), (0, -1), (1, 0), (-1, 0)), 2: ((1, 0), (-1, 0)),
                 3: ((0, 1), (0, -1)), 4: ((0, 1), (-1, 0)), 5: ((0, 1), (1, 0)),
                 6: ((0, -1), (1, 0)), 7: ((0, -1), (-1, 0))}
    res = bfs(R, C, L)

    print('#{} {}'.format(tc, res))