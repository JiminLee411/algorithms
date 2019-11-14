import sys
from pprint import pprint
sys.stdin = open('swep_5656_input.txt', 'r')

import copy
from collections import deque

def crush(x, y, n):
    if not n:
        return
    visited = [[0] * W for _ in range(H)]
    q = deque()
    q.append((x, y, pracStage[x][y]))
    visited[x][y] = 1
    while q:
        x, y, p = q.popleft()
        for dx in range(-p + 1, p):
            if 0 <= x + dx < W:
                if pracStage[x + dx][y] > 1:
                    q.append((x + dx, y, pracStage[x + dx][y]))
                pracStage[x + dx][y] = 0
        for dy in range(-p + 1, p):
            if 0 <= y + dy < H:
                if pracStage[x][y + dy] > 1:
                    q.append((x, y + dy, pracStage[x][y + dy]))
                pracStage[x][y + dy] = 0

    pprint(pracStage, width=W*10)
    print(n)

    crush()



T = int(input())
for tc in range(1, 2):
    N, W, H = map(int, input().split())
    stage = [list(map(int, input().split())) for _ in range(H)]
    visit = [0 for _ in range(W)]
    # print(visit)

    for r in range(H):
        for c in range(W):
            if not stage[r][c] or visit[c]:
                continue
            pracStage = copy.deepcopy(stage)
            dr = 1
            visit[c] = 1
            if pracStage[r][c] == 1:
                pracStage[r][c] = 0
                while r + dr < H and pracStage[r + dr][c] == 1:
                    pracStage[r + dr][c] = 0
                    dr += 1
                    if r + dr > H - 1 or N <= dr:
                        break
            else:
                dr = 0
            crush(r + dr, c, N - dr)
