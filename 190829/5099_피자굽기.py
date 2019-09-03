import sys

sys.stdin = open('5099_input.txt', 'r')

def baking(N, M):
    oven = [0] * N
    cntNum = 0
    cnt = [0] * N
    for i in range(N):
        oven[i] = cheezes.pop(0)
        cntNum += 1
        cnt[i] = cntNum
    while oven:
        for i in range(N):
            if oven[i] == 0:
                continue
            oven[i] = oven[i] // 2
            if oven[i] == 0:
                if cntNum < M:
                    oven[i] = cheezes.pop(0)
                    cntNum += 1
                    cnt[i] = cntNum
                else:
                    cnt[i] = 0
            if cnt.count(0) == N - 1:
                for i in cnt:
                    if i != 0: return i


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    cheezes = list(map(int, input().split()))
    res = baking(N, M)
    print('#{} {}'. format(t, res))