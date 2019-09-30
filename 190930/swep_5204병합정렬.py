import sys

sys.stdin = open('swep_5204_input.txt', 'r')


# 왼쪽, 오른쪽 더 큰 값을 찾아서 진행하는 방식.
def mergeSort(lo, hi):
    global ans
    if lo + 1 == hi:
        return arr[lo]
    mid = (lo + hi) >> 1
    l = mergeSort(lo, mid)
    r = mergeSort(mid, hi)
    if l > r:
        ans += 1
        return l
    else:
        return r

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    last = mergeSort(0, N)
    arr.sort()

    print('#{} {} {}'. format(tc, arr[N//2], ans))