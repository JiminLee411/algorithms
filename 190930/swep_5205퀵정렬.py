import sys

sys.stdin = open('swep_5205_input.txt', 'r')

def quickSort(lo, mid, hi):
    pass


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quickSort(0, N//2, N)

    # print('#{} {}'. format(tc, res))