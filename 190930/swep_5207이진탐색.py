import sys

sys.stdin = open('swep_5205_input.txt', 'r')

def binarySort(lo, hi):


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    binarySort(0, N - 1)

    print('#{} {}'. format(tc, arr[N//2]))

