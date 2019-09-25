import sys

sys.stdin = open('swep_5188input.txt', 'r')

def Go(r, c, cnt):
    global tmp
    if cnt == N*2 - 1:
        res.append(tmp)
        return
    for y, x in [(0, 1), (1, 0)]:
        if 0<=r+y<N and 0<=c+x<N:
            if res and (tmp + arr[r+y][c+x] >= min(res)):
                continue
            tmp += arr[r + y][c + x]
            Go(r+y, c+x, cnt + 1)
            tmp -= arr[r + y][c + x]


for tc in range(1, int(input()) + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    res = []
    tmp = arr[0][0]
    Go(0, 0, 1)
    print('#{} {}'. format(tc,min(res)))