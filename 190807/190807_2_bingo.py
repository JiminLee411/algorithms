import sys

sys.stdin = open('190807_2_input.txt')

board = []
bingoCount = 0
cnt = 0
# 5개를 따로 받아서 list에 저장한다.
for _ in range(5):
    row = list(map(int, input().split()))
    board.append(row)
    N = range(len(board[0]))
# 비교할 값을 리스트로 받아서 비교한다.
for _ in range(5):
    comp = list(map(int, input().split()))
    # 비교할 값을 하나를 뽑는다.
    for i in comp:
        for elem in range(5):
            if i in board[elem]:
                cnt += 1
                board[elem][board[elem].index(i)] = 0
                if cnt > 10:
                    sum_1, sum_2 = 0, 0
                    bingoCount = 0
                    for column in range(5):
                        if (board[column][0]==board[column][1]==board[column][2]==board[column][3]==board[column][4]==0):
                            bingoCount+=1
      
                    for row in range(5):
                        if (board[0][row]==board[1][row]==board[2][row]==board[3][row]==board[4][row]==0):
                            bingoCount+=1
  
                    if (board[0][0]==board[1][1]==board[2][2]==board[3][3]==board[4][4]==0):
                        bingoCount+=1
    
                    if (board[0][4]==board[1][3]==board[2][2]==board[3][1]==board[4][0]==0):
                        bingoCount+=1
                    if bingoCount >= 3:
                        print(cnt)
                        break
            if bingoCount >= 3:
                break
        if bingoCount >= 3:
            break
    if bingoCount >= 3:
        break

# board = []
# bingo_num = 0
# cnt = 0
# # 5개를 따로 받아서 list에 저장한다.
# for _ in range(5):
#     row = list(map(int, input().split()))
#     board.append(row)
#     N = range(len(board[0]))
# # 비교할 값을 리스트로 받아서 비교한다.
# for _ in range(5):
#     comp = list(map(int, input().split()))
#     # 비교할 값을 하나를 뽑는다.
#     for comp_i in comp:
#         cnt += 1
#         # 비교할 값이 빙고에 있는지 찾는다.
#         for j in range(5):
#             # 만약 빙고판에 비교할 값이 있다면
#             if comp_i in board[j]:
#                 # 해당 칸에 0을 넣는다
#                 board[j][board[j].index(comp_i)] = 0
#             # 만약 부른 숫자의 갯수가 10을 넘기면 비교한다
#             if cnt > 10:
#                 sum_1 = 0
#                 sum_2 = 0
#                 bingo_num = 0
#                 # row를 뽑는다
#                 for x in N:
#                     # colum을 뽑는다
#                     for y in N:
#                         # 만약 0이 있다면,
#                         if board[x][y] == 0:
#                             # 0이 있는 row의 합이 0인지 확인
#                             if sum(board[x][0:5]) == 0:
#                                 # 맞다면 빙고 + 1
#                                 bingo_num += 1
#                             # 0이 있는 column의 합이 0인지 확인
#                             if sum(board[0:5][y]) == 0:
#                                 # 맞다면 빙고 + 1
#                                 bingo_num += 1
#                     # 대각선 합 구하기
#                     sum_1 += board[x][x]
#                     sum_2 += board[x][-x-1]
#                 # 만약 0이면 빙고 + 1
#                 if sum_1 == 0:
#                     bingo_num += 1
#                 if sum_2 == 0:
#                     bingo_num += 1
#                 # 만약 빙고 합이 3이상이면 탈출!
#                 if bingo_num >= 3:
#                     print(cnt)
#                     break
#             if bingo_num >= 3:
#                 break
#         if bingo_num >= 3:
#             break
#     if bingo_num >= 3:
#         break





