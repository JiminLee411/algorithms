import sys

sys.stdin = open('Ladder_input.txt', 'r')

for _ in range(10):
    t = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    X = board[99].index(2)

    for i in range(98, -1, -1):
        if X != 0 and board[i][X - 1] == 1:
            while board[i][X - 1] == 1:
                if X == 1:
                    X = 0
                    break
                X -= 1
        elif X != 99 and board[i][X + 1] == 1:
            while board[i][X + 1] == 1:
                if X == 98:
                    X = 99
                    break
                X += 1
    print('#{} {}'. format(t, X))