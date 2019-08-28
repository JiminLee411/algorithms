import sys
sys.stdin = open('input.txt', 'r')


# def tournament(start, end):
#     if end > 1:
#         tmp.append(tournament(start, end // 2))
#         tmp.append(tournament(end // 2 + 1, end))
#     if cards[start] >= cards[end] or (cards[start] == 1 and cards[end] == 3):
#         return start
#     elif cards[start] < cards[end] or (cards[start] == 3 and cards[end] == 1):
#         return end
#     else:
#         return end
#
#
# for t in range(1, int(input()) + 1):
#     N = int(input())
#     cards = list(map(int, input().split()))
#     tmp = []
#     tournament(0, len(cards) // 2)
#     res = tournament(len(cards) // 2 + 1, len(cards) - 1)
#     print(res)


def tournament(start, end):
    if end - start > 1:
        tmp2.append(tournament(start, (start + end) // 2))
        tmp2.append(tournament((start + end) // 2 + 1, end))
    else:
        if cards[start] >= cards[end] or (cards[start] == 1 and cards[end] == 3):
            return start
        elif cards[start] < cards[end] or (cards[start] == 3 and cards[end] == 1):
            return end
        else:
            return start


for t in range(1, 2):
    N = 4
    cards = [1, 3, 2, 1]
    tmp1 = [i for i in range(N)]

    while len(tmp1) > 1:
        tmp2 = []
        tmp2.append(tournament(0, (len(cards) - 1) // 2))
        tmp2.append(tournament((len(cards) - 1) // 2 + 1, len(cards) - 1))

    print(tmp)


# for t in range(1, int(input()) + 1):
#     N = int(input())
#     cards = list(map(int, input().split()))
#     tmp1 = [i for i in range(N)]
#
#     while len(tmp1) > 1:
#         tmp2 = []
#         for i in range(0, len(tmp1), 2):
#             if (len(tmp1) % 2 == 1 and i == len(tmp1) - 1):
#                 tmp2.append(tmp1[i])
#                 break
#             elif (cards[tmp1[i]] == 1 and cards[tmp1[i + 1]] == 3) or cards[tmp1[i]] >= cards[tmp1[i + 1]]:
#                 tmp2.append(tmp1[i])
#             elif (cards[tmp1[i]] == 3 and cards[tmp1[i + 1]] == 1) or cards[tmp1[i]] < cards[tmp1[i + 1]]:
#                 tmp2.append(tmp1[i + 1])
#         tmp1 = list(tmp2)
#     print('#{} {}'. format(t, tmp1[0] + 1))




