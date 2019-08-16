import sys

sys.stdin = open('4861_input.txt', 'r')
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    board = []
    res = ''
    tmp = ''

    for _ in range(N):
        string = input()

        for i in range(N - M + 1):
            tmp = string[i : i + M]
            if tmp == tmp[::-1]:
                res = tmp

        board.append(string)

    # 만약 res가 빈 문자열이면
    if not res:
        for column in range(N):
            tmp = ''

            if res:
                break

            for row in range(N):
                # 남은 비교값이 아직 M길이에 비해 길고 row 값과 row + M -1 이 같으면
                if (row <= N - M) & (board[row][column] == board[row + M - 1][column]):
                    for i in range(M):
                        # 서로 같으면
                        if board[row + i][column] == board[row + M - i - 1][column]:
                            tmp += board[row + i][column]
                            # 만약 tmp 길이가 M이 된다면
                            if len(tmp) == M:
                                res = tmp
                                break
                        # 서로 다르면
                        else:
                            tmp = ''
                            break
                else:
                    tmp = ''
                # 앞으로의 길이는 M보다 작으므로 결과가 없으므로 나간다.
                if row >= N - M:
                    tmp = ''
                    break

    print('#{} {}'. format(tc, res))