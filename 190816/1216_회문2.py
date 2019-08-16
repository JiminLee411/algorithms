import sys

sys.stdin = open('1216_input2.txt', 'r')

def compp (board):
    MaxLen = 0
    for row in range(100):
        # 앞자리0부터 99까지
        for front in range(100):
            # 뒷자리 99부터 front까지
            for end in range(99, front, -1):
                # 총 길이 설정
                Len = end - front + 1
                # max보다 len이 짧다면 나간다.
                if MaxLen >= Len:
                    break
                # front부터 end 길이 만큼을 슬라이싱해서 reverse한거와 비교
                comp1 = board[row][front: end + 1]
                comp2 = comp1[::-1]
                # 만약 같다면
                if comp1 == comp2:
                    # res길이보다 comp1 길이가 더 크면 res = comp1
                    if MaxLen < Len:
                        MaxLen = Len
                        break
    return MaxLen

for _ in range(1, 11):
    board = []
    tc = input()
    board = [input() for _ in range(100)]

    res = compp(board)

    # column 받으면서 비교
    transpose_board = list(zip(*board))

    res = max(res, compp(transpose_board))

    print('#{} {}'. format(tc, res))
