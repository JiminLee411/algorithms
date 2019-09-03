import sys
sys.stdin = open('5105_input.txt', 'r')

def BFS(r, c, n):
    Q = []
    Q.append([r, c])
    visit[r][c] = 1
    D[r][c] = 0

    while Q:
        r, c = map(int, Q.pop(0))

        for y, x in zip([0,0,-1,1], [-1,1,0,0]):
            if r + y > n - 1 or r + y < 0 or c + x > n - 1 or c + x < 0:
                continue
            elif maze[r + y][c + x] == '0' and not visit[r + y][c + x]:
                Q.append([r + y, c + x])
                visit[r + y][c + x] = 1
                D[r + y][c + x] = D[r][c] + 1
            elif maze[r + y][c + x] == '3':
                return D[r][c]
    return 0

for t in range(1, int(input()) + 1):
    N = int(input())
    maze = [input() for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    D = [[0] * N for _ in range(N)]

    for row in range(N):
        if '2' in maze[row]:
            s_row, s_col = row, maze[row].index('2')
            break

    res = BFS(s_row, s_col, N)

    print('#{} {}'. format(t, res))