import sys

sys.stdin = open('swep_5201input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    N_w = sorted(list(map(int, input().split())))
    max_w = sorted(list(map(int, input().split())))
    N_w.reverse()
    max_w.reverse()
    fin = [0 for _ in range(N)]
    res = tmp = 0

    for i in range(M):
        for j in range(N):
            if not fin[j] and max_w[i] >= N_w[j]:
                fin[j] = 1
                tmp += N_w[j]
                break

    if res < tmp:
        res = tmp

    print('#{} {}'. format(tc, res))
