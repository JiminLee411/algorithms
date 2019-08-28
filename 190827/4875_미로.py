import sys
sys.stdin = open('4875_input.txt', 'r')

def DFS(r, c, n):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    visit[r][c] = True
    for i in range(4):
        if r + dy[i] > n - 1 or r + dy[i] < 0 or c + dx[i] > n - 1 or c + dx[i] < 0:
            continue
        elif maze[r + dy[i]][c + dx[i]] == '3':
            return 1
        elif (visit[r + dy[i]][c + dx[i]] == False) and maze[r + dy[i]][c + dx[i]] == '0':
            if DFS(r + dy[i], c + dx[i], n) == 1:
                return 1
    return 0

for t in range(1, int(input()) + 1):
    N = int(input())
    maze = [input() for _ in range(N)]
    visit = [[False] * N for _ in range(N)]
    res = 0
    for i in range(N):
        if '2' in maze[i]:
            column = maze[i].find('2')
            row = i
            break
    res = DFS(row, column, N)
    print('#{} {}'. format(t, res))

# 선생님 코드
# def DFS(x, y):
#     if maze[x][y] == '3' : return True
#
#     maze[x][y] = '1'
#
#     for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#         tx, ty = x + dx, y + dy
#         if tx < 0 or tx == N or ty < 0 or ty == N or maze[tx][ty] == '1' : continue
#         if DFS(tx, ty):
#             maze[x][y] = '0'
#             return True
#
#         maze[x][y] = '0'
#         return False
