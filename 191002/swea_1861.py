import sys

sys.stdin = open('swep_1861_input.txt', 'r')

def back(x,y,cnt,sx,sy):
    global Max,sp
    if Max<cnt:
        Max = max(Max, cnt)
        sp = board[sx][sy]
    for dx,dy in (1,0),(0,1),(-1,0),(0,-1):
        nx,ny = x+dx,y+dy
        if 0<=nx<N and 0<=ny<N and board[nx][ny]-board[x][y]==1:
            back(nx, ny, cnt+1,sx,sy)

T = int(input())

for t in range(1,T+1):
    N = int(input())
    board= [list(map(int, input().split())) for _ in range(N)]
    Max = 0
    sp = 0
    for i in range(N):
        for j in range(N):
            back(i, j, 1,i,j)
    print(sp, Max)