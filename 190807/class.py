# list1 = [[0] * 3] * 3
# list1[0][0] = 1
# print(list) # => [[1,0,0],[1,0,0],[1,0,0]]
#
# list2 = [[0] * 3 for i in range(3)]
# list2[0][0] = 1
# print(list2) # => [[1,0,0],[0,0,0],[0,0,0]]
#
# arr1 = [[1,2],[3,4]]
# arr2 = [arr1[0]]
# arr1[0][0] = 100
# print(arr1) # => [[100,2], [3,4]]
# print(arr2) # => [[100,2]]
#
# # 지그재그 순회
# arr = [[1, 2], [3, 4]]
# N = len(arr)
# for i in arr:
#     if i % 2 == 0: # 짝수 : ------>
#         for j in range(N):
#             pass
#     else:          # 홀수 : <-------
#         for j in range(N-1, -1, -1):
#             pass
#
# #  대각선 순회
# N, M = len(arr), len(arr[0])
# for diag in range(0, N + M -1):
#     x = 0 if diag < M else (diag - M + 1)
#     y = diag if diag < M else M-1
#
#     while x < N and y >= 0:
#         print('%2d ' % arr[x][y], end='')
#         x += 1
#         y -= 1
#
# a = 0b1010
# print(bin(a >> 2))
#
# n = 10
# if n & 1:
#     print('홀수')
# else:
#     print('짝수')
#
# # 이진검색 알고리즘
# def binaryearch(arr, key):
#     lo, hi = 0, len(arr) -1
#     # lo = 범위의 시작 인덱스, hi = 범위의 끝 인덱스
#     while lo <= hi:
#         mid = (lo + hi) >> 1
#         if arr[mid] == key:
#              return True
#         elif arr[mid] > key:
#             hi = mid - 1
#         else:
#             lo = mid + 1
#     return False
#
# # 이진 검색 알고리즘 - 재귀함수
# def binarySearch(arr, lo, hi, key):
#     if lo > hi: return False
#
#     mid = (lo + hi) >> 1
#
#     if arr[mid] == key:
#          return True
#     elif arr[mid] > key:
#         return binarySearch(arr, lo, mid -1 , key)
#     else:
#         return binarySearch(arr, mid + 1, hi, key)

arr = [64, 25, 10, 22, 11]
n = len(arr)
# 첫번째 단계 [0, n - 1]
for i in range(n - 1):
    minIdx = i
    for j in range(i + 1, n):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]

print(arr)

