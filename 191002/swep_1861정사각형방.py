import sys

sys.stdin = open('swep_1861_input.txt', 'r')

def DFS(r, c):
    global MAX, cnt
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= r + dr < N and 0 <= c + dc < N and rooms[r][c] + 1 == rooms[r + dr][c + dc]:
            cnt += 1
            DFS(r + dr, c + dc)


for tc in range(1, int(input()) + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    MAX = 0
    for r in range(N):
        for c in range(N):
            cnt = 0
            DFS(r, c)
            if MAX < cnt:
                MAX = cnt
                room = rooms[r][c]
            elif MAX == cnt and room > rooms[r][c]:
                MAX = cnt
                room = rooms[r][c]

    print('#{} {} {}'. format(tc, room, MAX + 1))
