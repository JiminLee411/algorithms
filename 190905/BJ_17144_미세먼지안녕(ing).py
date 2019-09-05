import sys
import operator

sys.stdin = open('BJ_17144_input.txt', 'r')

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
spread = [[0 for _ in range(C)] for _ in range(R)]

for r in range(R):
    for c in range(C):
        if room[r][c] > 0:
            dust = room[r][c] // 5
            for y, x in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
                if (r + y < 0 or r + y >= R) or (c + x < 0 or c + x >= C):
                    continue
                if room[r + y][c + x] >= 0:
                    spread[r + y][c + x] += dust
                    room[r][c] -= dust
for r in range(R):
    room[r] = list(map(operator.add,room[r],spread[r]))

# 공기청정기 바람 추가 작성 필요
