import sys

sys.stdin = open('4836_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 10X10의 0이 들어간 2차원 배열을 만든다
    board = [[0] * 10 for _ in range(10)]
    purple = 0

    for num in range(N):
        # 받을 리스트를 선언 및 초기화 해준다.
        value = []
        # 값을 한 줄의 1차원 리스트로 받는다
        value = list(map(int, input().split()))
        # 만약 받은 1차원 리스트 마지막 숫자가 1이면
        if value[-1] == 1:
            # left_x부터 right_x까지의 값을 뽑아낸다
            for x in range(value[0], value[2] + 1):
                # left_y부터 right_y까지의 값을 뽑아낸다
                for y in range(value[1], value[3] + 1):
                    # x,y 를 조합하여 거기에 1을 더해준다.
                    board[x][y] += 1
        # 만약 숫자가 1이 아니라면
        else:
            for x in range(value[0], value[2] + 1):
                for y in range(value[1], value[3] + 1):
                    # 2를 더해준다.
                    board[x][y] += 2
    for i in range(10):
        # board에 3인 값을 카운트해서 더한다.
        purple += board[i].count(3)
    print('#{} {}'. format(tc, purple))




