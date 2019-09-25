# 병합정렬 --> 연결리스트에 적합
# python List append(), pop(), slicing을 사용하면 시간이 너무 오래 소요됨
arr = [69, 10, 30, 2, 16, 8, 31, 22]
tmp = [0] * len(arr)

def mergeSort(lo, hi):  # 문제의 크기 - 정렬할 자료의 범위
    if lo == hi : return
    # 유도 사례
    mid = (lo + hi) >> 1
    mergeSort(lo, mid)
    mergeSort(mid + 1, hi)
    # 왼쪽과 오른쪽 자료들이 정렬된 상태
    i, j, k = lo, mid + 1, lo
    while i <=mid and j <=hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            k, i = k + 1, i + 1
        else:
            tmp[k] = arr[j]
            k, j = k + 1, j + 1
    while i <= mid:
        tmp[k] = arr[i]
        k, i = k + 1, i + 1
    while j <= hi:
        tmp[k] = arr[j]
        k, j = k + 1, j + 1
    for  x in range(lo, hi + 1):
        arr[x] = tmp[x]


mergeSort(0, len(arr) - 1)
print(arr)


# 퀵 정렬
arr = [69, 10, 30, 2, 16, 8, 31, 22]

def quickSort(lo, hi):
    if lo >= hi: return

    # 피봇을 정해서 파티션 알고리즘 수행
    i, j = lo, hi   #arr[lo] : 피봇
    while i < j:
        while i <= hi and arr[lo] >= arr[i]: i += 1
        while arr[lo] < arr[j]: j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        arr[lo], arr[j] = arr[j], arr[lo]   # 피봇이 있어야할 위치로

    quickSort(lo, j - 1)
    quickSort(j + 1, hi)
print(arr)
quickSort(0, len(arr) - 1)
print(arr)

# 퀵 정렬 2
arr = [69, 10, 30, 2, 16, 8, 31, 22]

def quickSort(lo, hi):
    if lo >= hi: return
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] < arr[hi]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[hi] = arr[hi], arr[i]

    quickSort(lo, j - 1)
    quickSort(i + 1, hi)
print(arr)
quickSort(0, len(arr) - 1)
print(arr)