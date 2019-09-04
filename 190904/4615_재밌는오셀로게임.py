import sys

sys.stdin = open('4615_input.txt', 'r')

def check(cr, cc, n, turn):
    if turn == 1: next = 2
    else: next = 1
    for r in range(-1,2):
        for c in range(-1,2):
            i = 1
            while (-1 < cr+r*i < n) and (-1 < cc+c*i < n) and board[cr + r*i][cc + c*i] == next:
                if (-1 < cr+r*(i+1) < n) and (-1 < cc+c*(i+1) < n) and board[cr + r*(i+1)][cc + c*(i+1)] == turn:
                    for j in range(1, i + 2):
                        board[cr + r*j][cc + c*j] = turn
                i += 1


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [[0 for c in range(N)] for r in range(N)]
    b = w = 0
    board[(N>>1) - 1][(N>>1) - 1] = 2
    board[(N>>1) - 1][N>>1] = 1
    board[N>>1][(N>>1) - 1] = 1
    board[N>>1][N>>1] = 2

    for _ in range(M):
        r,c,turn = map(int, input().split())
        board[r - 1][c - 1] = turn
        check(r - 1, c - 1, N, turn)
    for i in range(N):
        b += board[i].count(1)
        w += board[i].count(2)
    print('#{} {} {}'. format(t, b, w))
