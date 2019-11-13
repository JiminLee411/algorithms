import sys
sys.stdin = open('swep_2117.txt', 'r')


from collections import deque

delta = ((1, 0), (-1, 0), (0, 1), (0, -1))
def find(x, y):
    global homeCnt
    visited = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    visited[x][y] = 1
    cnt = city[x][y]
    Q = deque()
    Q.append([r, c])
    k = 1
    while Q:
        x, y = Q.popleft()
        if visited[x][y] == N + 1:
            break
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                if visited[nx][ny] > k:
                    k = visited[nx][ny]
                Q.append([nx, ny])
                if city[nx][ny]:
                    cnt += 1

        if cnt*M - (k*k + (k-1)*(k-1)) >= 0 and homeCnt < cnt:
            homeCnt = cnt

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    homeCnt= 1
    for r in range(N):
        for c in range(N):
            find(r, c)

    print('#{} {}'. format(tc, homeCnt))