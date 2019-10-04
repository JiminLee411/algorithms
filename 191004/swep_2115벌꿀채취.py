import sys

sys.stdin = open('swep_2115_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M, C = map(int, input().split())
    honeyBox = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    honey = [[0] * (N - M  + 1) for _ in range(N)]
    for i in range(N):
        for j in range(N - M + 1):
            choose = sorted(honeyBox[i][j:j + M])[::-1]
            honeyCnt = res = MAX = 0
            for x in range(M):
                honeyCnt = res = 0
                for xx in range(x, M):
                    if choose[xx] <= C and honeyCnt + choose[xx] <= C:
                        honeyCnt += choose[xx]
                        res += choose[xx] * choose[xx]
                    else:
                        continue
                MAX = max(MAX, res)
            honey[i][j] = MAX
    MAX2 = 0
    for r in range(N):
        for c in range(N - M + 1):
            res = honey[r][c]
            for secondR in range(r, N):
                for secondC in zzzrange(N - M + 1):
                    if r == secondR and secondC < c + M:
                        continue
                    res += honey[secondR][secondC]
                    MAX2 = max(MAX2, res)
                    res -= honey[secondR][secondC]

    print('#{} {}'. format(tc, MAX2))