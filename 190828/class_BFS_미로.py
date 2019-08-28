import sys
sys.stdin = open("BFS_미로_input.txt", "r")

def BFS(r, c, n):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    # 큐를 생성, 방문 표시
    Q = []
    visit[r][c] = 1
    Q.append([r,c])
    while Q:
        r, c = map(int, Q.pop(0))
        for i in range(4):
            if r + dy[i] > n - 1 or r + dy[i] < 0 or c + dx[i] > n - 1 or c + dx[i] < 0:
                continue
            elif maze[r + dy[i]][c + dx[i]] == '3':
                return 1
            elif (visit[r + dy[i]][c + dx[i]] == 0) and maze[r + dy[i]][c + dx[i]] == '0':
                visit[r + dy[i]][c + dx[i]] = 1
                for j in visit:
                    print(j)
                print()
                Q.append([r + dy[i], c + dx[i]])
                # print(Q)
                # print()
    return 0

for t in range(1, int(input()) + 1):
    N = int(input())
    maze = [input() for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    for row in range(N):
        if '2' in maze[row]:
            r, c = row, maze[row].find('2')
            break
    res = BFS(r, c, N)
    print(res)
