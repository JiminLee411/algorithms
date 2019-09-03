import sys

sys.stdin = open('6109_input.txt', 'r')
def up(n):
    for r in range(n):
        for c in range(n - 1, 0, -1):
            if board[r][c] == 0:
                board[r].pop(c)
                board[r].appendleft(0)
            if board[r][c] == board[r][c-1]:
                board[r][c] += board[r].pop(c - 1)
                board[r].appendleft(0)
                print(board)
def down():
    pass
def left(n):
    for c in range(n - 1):
        if tmp[c] == 0:
            tmp.append(tmp.pop(c))
        if tmp[c] == tmp[c+1]:
            tmp[c] += tmp.pop(c+1)
            tmp.append(0)

def right(n):
    global tmp
    for c in range(n - 1, 0, -1):
        if tmp[c] == 0:
            tmp.pop(c)
            tmp = [0] + tmp
            if tmp[c] == 0:

        if tmp[c] == tmp[c-1]:
            tmp[c - 1] += tmp.pop(c)
            tmp = [0] + tmp
        print(tmp)


for t in range(1,int(input()) + 1):
    N, S = map(str, input().split())
    N = int(N)
    board = []

    for _ in range(N):
        tmp = list(map(int, input().split()))
        if S == 'left':
            left(N)
            board.append(' '.join(list(map(str, tmp))))
            print(board)

        elif S == 'up':
            right(N)
            board.append(' '.join(list(map(str, tmp))))
            print(board)
    if S == 'up':
        pass
    elif S == 'down':
        pass
