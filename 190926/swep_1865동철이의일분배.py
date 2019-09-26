import sys

sys.stdin = open('swep_1865_input.txt', 'r')

def Choose(n, tmp, used):
        global res
    if tmp < res or tmp == 0: return
    if n == N:
        if res < tmp:
            res = tmp
            return
    for i in range(N):
        if used & 1<<i:
            continue
        Choose(n + 1, tmp*arr[n][i], used|1<<i)

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(lambda x:int(x)/100, input().split())) for _ in range(N)]
    res = 0
    Choose(0, 1, 0)
    print('#{} {:.6f}'. format(tc, res*100))