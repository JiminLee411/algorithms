import sys

sys.stdin = open('회문_input.txt', 'r')

def compp (N, board):
    cnt = 0
    for row in range(8):
        for i in range(8 - N + 1):
            tmp = board[row][i: i + N]
            if tmp == tmp[::-1]:
                cnt += 1
    return cnt


for tc in range(1, 11):
    board = []
    N = int(input())
    board = [input() for _ in range(8)]

    cnt = compp(N, board)

    # column 받으면서 비교
    transpose_board = list(zip(*board))

    cnt += compp(N, transpose_board)

    print('#{} {}'. format(tc, cnt))
