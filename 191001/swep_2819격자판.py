# 선생님
import sys

sys.stdin = open('swep_2819_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    pan = [list(input().split()) for _ in range(4)]

    def backtrack(x, y, n, key):
        if n == 7:
            global ans
            if key not in dic:
                dic[key] = 1
                ans += 1
                return 1
            return 0
        else:
            ret = 0
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                tx, ty = x + dx, y + dy
                if 0 <= tx < 4 and 0 <= ty < 4:
                    backtrack(tx, ty, n + 1, key + pan[tx][ty])

    dic = dict()
    ans = ret = 0
    for i in range(4):
        for j in range(4):
            backtrack(i, j, 1, pan[i][j])

    print('#{} {}'. format(tc, ans))