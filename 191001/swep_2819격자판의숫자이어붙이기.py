import sys

sys.stdin = open('swep_2819_input.txt', 'r')

# def DFS(r, c, k):
#     global cnt, tmp
#     if k == 7:
#         storage.add(''.join(tmp))
#         return
#
#     for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#         if 0 <= r + x < 4 and 0 <= c + y < 4:
#             tmp.append(str(arr[r + x][c + y]))
#             DFS(r + x, c + y, k + 1)
#             tmp.pop()
#
# for tc in range(1, int(input()) + 1):
#     arr = [list(map(int, input().split())) for _ in range(4)]
#     storage = set()
#     tmp = []
#     cnt = 0
#     for r in range(4):
#         for c in range(4):
#             DFS(r, c, 0)
#     print('#{} {}'. format(tc, len(storage)))

def find(x, y, k):
    if len(k) == 7:
        s.add(k)
        return
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
        tx, ty = x + dx, y + dy
        if 0 <= tx < 4 and 0 <= ty < 4:
            find(tx, ty, k + arr[tx][ty])


T = int(input())
for t in range(1, T + 1):
    arr = [list(input().split()) for _ in range(4)]
    s = set()
    for r in range(4):
        for c in range(4):
            find(r, c, '')
    print('#{} {}'.format(t, len(s)))


# s = set()
# def find(k, x, y):
#     if k == 7:
#         s.add(''.join(tmp))
#         return
#     for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#         tx, ty = x + dy, y + dx
#         if 0 <= tx < 4 and 0 <= ty < 4:
#             tmp.append(str(arr[tx][ty]))
#             find(k+1, tx, ty)
#             tmp.pop()
#
# T = int(input())
# for t in range(1, T+1):
#     arr = [list(map(int, input().split())) for _ in range(4)]
#     tmp = []
#     for row in range(4):
#         for column in range(4):
#             find(0, row, column)
#     print('#{} {}'.format(t, len(s)))