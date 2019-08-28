import sys

sys.stdin = open('1220_input.txt', 'r')

# for t in range(1, 11):
#     N = int(input())
#     table = [list(map(int, input().split())) for _ in range(N)]
#     cnt = 0
#     for column in range(N):
#         tmp1 = tmp2 = []
#         for row in range(N >> 1):
#             val1, val2 = table[row][column], table[N - row - 1][column]
#             if not tmp1 and val1 == 2:
#                 table[row][column] = 0
#             elif val1 != 0:
#                 tmp1.append(val1)
#
#             if not tmp2 and val2 == 1:
#                 table[N - row - 1][column] = 0
#             elif val2 != 0:
#                 tmp2.append(val2)
#
#         tmp2.reverse()
#         tmp1.extend(tmp2)
#
#         tmp = 0
#         for i in tmp1:
#             if tmp == 0 and i == 1:
#                 tmp = 1
#             elif tmp == 1 and i == 2:
#                 tmp = 0
#                 cnt += 1
#     print('#{} {}'. format(t, cnt))

######################################################################
for t in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    tmp = 0
    for column in range(N):
        for row in range(N):
            if table[row][column] == 1 and tmp == 0:
                tmp = 1
            if table[row][column] == 2 and tmp == 1:
                cnt += 1
                tmp = 0
    print('#{} {}'. format(t, cnt))
