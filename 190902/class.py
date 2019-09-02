# 단순 연결 리스트의 삽입 연산

# 삽입 정렬
# arr = [69, 10, 30, 2, 16, 8, 31, 22]
# N = len(arr)
#
# # 삽입하는 작업을 n-1번 반복 (1번 ~ n-1번)
# for i in range(1, N):
#     tmp = arr[i] # 정렬할 값
#     j = i - 1 # 비교할 인덱스
#     while j >= 0 and arr[j] > tmp:
#         arr[j + 1] = arr[j]
#         j -= 1
#     arr[j + 1] = tmp
#
# print(arr)

# 병합 정렬
arr2 = [69, 10, 30, 2, 16, 8, 31, 22]
tmp = [0] * len(arr2) # 비교후 옮겨적을 배열

def mergeSort(lo, hi):
    if lo >= hi: return
    mid = (lo + hi) >> 1
    mergeSort(lo, mid)
    mergeSort(mid + 1, hi)

    i, j, k = lo, mid + 1, lo
    while i <= mid and j <= hi:
        if arr2[i] < arr2[j]:
            tmp[k] = arr2[i]
            k, i = k + 1, i + 1
        else:
            tmp[k] = arr2[j]
            k, j = k + 1, j + 1

    while i <= mid:
        tmp[k] = arr2[i]
        k, i = k + 1, i + 1
    while j <= hi:
        tmp[k] = arr2[j]
        k, j = k + 1, j + 1
    for i in range(lo, hi + 1):
        arr2[i] = tmp[i]
    print(arr2) # 정렬과정 보여줌

mergeSort(0, len(arr2) - 1) # 정렬해야할 시작과 끝을 넣는다.
print(arr2) # 결과