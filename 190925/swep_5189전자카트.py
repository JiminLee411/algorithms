import sys

sys.stdin = open('swep_5189input.txt', 'r')

def Check(r, cnt):
    global res, tmp
    if cnt == N:
        if res > tmp:
            res = tmp
        return
    for i in range(N):
        if i == r or visit[0][i] or visit[1][r]:
            continue
        visit[0][i], visit[1][r] = 1, 1
        tmp += arr[r][i]
        Check(i, cnt + 1)
        tmp -= arr[r][i]
        visit[0][i], visit[1][r] = 0, 0

for tc in range(1, int(input()) + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0 for _ in range(N)] for _ in range(2)]
    tmp, res = 0, 0xfffff

    Check(0, 0)
    print('#{} {}'. format(tc, res))