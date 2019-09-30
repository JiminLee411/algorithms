import sys

sys.stdin = open('swep_5205_input.txt', 'r')

def quickSort(lo, hi):
    if lo >= hi:return
    i, j = lo,hi
    while i < j:
        while i<=hi and arr[i] <= arr[lo]:
            i+=1
        while arr[j] >arr[lo]:
            j-=1
        if i>=j: break
        arr[i], arr[j] = arr[j],arr[i]
    arr[j] ,arr[lo] = arr[lo],arr[j]

    quickSort(lo,j-1)
    quickSort(j+1, hi)

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quickSort(0, N - 1)

    print('#{} {}'. format(tc, arr[N//2]))

